from functools import reduce
import operator

from django.core.urlresolvers import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView, DetailView, FormView, UpdateView, DeleteView

from BMS_app.forms import PersonalInformationForm, RelativeInformationForm, UpdateForm
from BMS_app.models import PersonalInformation, FamilyMemberInformation


class Index(TemplateView):
    template_name = 'homepage.html'


class ListAll(ListView):
    template_name = 'listall.html'
    model = PersonalInformation


class About(TemplateView):
    template_name = 'about.html'


class CreatePerson(CreateView):
    model = PersonalInformation
    template_name = 'create.html'
    form_class = PersonalInformationForm
    success_url = reverse_lazy('BMS_app:ListAll')


class UpdatePerson(UpdateView):
    model = PersonalInformation
    form_class = UpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('BMS_app:ListAll')
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super(UpdatePerson, self).get_context_data(**kwargs)
        context['pk_person_id'] = PersonalInformation.objects.get(id=self.kwargs['pk'])
        return context


class DeletePerson(DeleteView):
    model = PersonalInformation
    success_url = reverse_lazy('BMS_app:ListAll')
    template_name = 'delete.html'


class PersonDetails(DetailView):
    template_name = 'details.html'
    context_object_name = 'relatives'

    def get_object(self, queryset=None):
        person = PersonalInformation.objects.get(id=self.kwargs['pk'])
        relatives = FamilyMemberInformation.objects.filter(person_id=person.id)
        return relatives

    def get_context_data(self, **kwargs):
        context = super(PersonDetails, self).get_context_data(**kwargs)
        context['pk_id'] = PersonalInformation.objects.get(id=self.kwargs['pk'])
        return context


class RelativeCreate(FormView):
    model = FamilyMemberInformation
    template_name = 'create_relative.html'
    form_class = RelativeInformationForm

    def get_success_url(self):
        return reverse('BMS_app:PersonDetails', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        relative = form.save(commit=False)
        relative.person_id = self.kwargs['pk']
        relative.save()

        return super(RelativeCreate, self).form_valid(form)


class UpdateRelative(UpdateView):
    model = FamilyMemberInformation
    form_class = UpdateForm
    template_name = 'updaterelative.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateRelative, self).get_context_data(**kwargs)
        context['pk_person_id'] = FamilyMemberInformation.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('BMS_app:PersonDetails')


class DeleteRelative(DeleteView):
    model = FamilyMemberInformation
    success_url = reverse_lazy('BMS_app:ListAll')
    template_name = 'delete.html'


class BlogSearchListView(ListView):
    paginate_by = 10
    template_name = 'results.html'
    model = PersonalInformation

    def get_queryset(self):
        result = super(BlogSearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            from django.db.models import Q
            result  = result.filter(
                reduce(operator.add,
                       (Q(first_name__icontains=q) for q in query_list)) |
                reduce(operator.add,
                       (Q(email__icontains=q) for q in query_list))
            )

            return result

