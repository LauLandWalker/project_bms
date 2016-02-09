from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from BMS_app.models import PersonalInformation, FamilyMemberInformation


class PersonalInformationForm(forms.ModelForm):
    dob = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date of Birth',
                                                        'type': 'date',
                                                        }))

    age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number',
                                                        'maxlength': '3',
                                                        'min': '1',
                                                        'max': '100'
                                                        }))

    contact_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel',
                                                                   'minlength': '7',
                                                                   'maxlength': '11',
                                                                   }))

    class Meta:
        model = PersonalInformation
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'dob',
            'gender',
            'civil_status',
            'address',
            'contact_number',
            'email',
        )


# Added
class UpdateForm(forms.ModelForm):
    dob = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date of Birth',
                                                        'type': 'date',
                                                        }))

    age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number',
                                                        'maxlength': '3',
                                                        'min': '1',
                                                        'max': '100'
                                                        }))

    contact_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel',
                                                                   'minlength': '7',
                                                                   'maxlength': '11',
                                                                   }))

    class Meta:
        model = PersonalInformation
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'dob',
            'gender',
            'civil_status',
            'address',
            'contact_number',
            'email',
        )













class RelativeInformationForm(forms.ModelForm):
    dob = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date of Birth',
                                                        'type': 'date',
                                                        }))

    age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number',
                                                        'maxlength': '3',
                                                        'min': '1',
                                                        'max': '100'
                                                        }))

    contact_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel',
                                                                   'minlength': '7',
                                                                   'maxlength': '11',
                                                                   }))

    # person_id = ModelChoiceField(queryset=PersonalInformation.objects.all())


    class Meta:
        model = FamilyMemberInformation
        fields = (
            # 'person_id',
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'dob',
            'gender',
            'relation',
            'civil_status',
            'address',
            'contact_number',
            'email',
        )
        #
        # def __init__(self, *args, **kwargs):
        #     super(FamilyMemberInformation, self).__init__(*args, **kwargs)
        #     self.fields['person_id'].widget = Select(attrs={'style':'background_color:#F5F8EC'})


        class UserCreationForm(UserCreationForm):

            class Meta:

                Model = User


