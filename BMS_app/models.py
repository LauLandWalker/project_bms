from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PersonalInformation(models.Model):
    first_name = models.CharField('First Name', max_length=100, null=False)
    middle_name = models.CharField('Middle Name', max_length=100, null=False)
    last_name = models.CharField('Last Name', max_length=100, null=False)
    age = models.IntegerField('Age', validators=[MinValueValidator(1), MaxValueValidator(100)], null=False)
    dob = models.DateField()

    # gender choices
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
    )

    gender = models.CharField('Gender', max_length=6, choices=GENDER, null=False)

    # civil status choices
    CIVIL_STATUS = (
        ('Married', 'married'),
        ('Single', 'single'),
    )

    civil_status = models.CharField('Civil Status', max_length=7, choices=CIVIL_STATUS, null=False)
    address = models.CharField('Address', max_length=120, null=False)
    contact_number = models.IntegerField('Contact Number', null=False)
    email = models.EmailField('Email', null=False)

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'middle_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(PersonalInformation, self).save(*args, **kwargs)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])


class FamilyMemberInformation(models.Model):
    person = models.ForeignKey(PersonalInformation, null=True)
    first_name = models.CharField('First Name', max_length=100, null=False)
    middle_name = models.CharField('Middle Name', max_length=100, null=False)
    last_name = models.CharField('Last Name', max_length=100, null=False)
    age = models.IntegerField('Age', validators=[MinValueValidator(1), MaxValueValidator(100)], null=False)
    dob = models.DateField('Birthday', null=False)

    # gender choices
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
    )

    gender = models.CharField('Gender', max_length=6, choices=GENDER, null=False)


    # relation
    RELATION = (
        ('Mother', 'mother'),
        ('Father', 'father'),
        ('Father', 'siblings'),
    )

    relation = models.CharField('Relation', max_length=9, choices=RELATION, null=False)


    # civil status choices
    CIVIL_STATUS = (
        ('Married', 'married'),
        ('Single', 'single'),
    )

    civil_status = models.CharField('Civil Status', max_length=7, choices=CIVIL_STATUS, null=False)
    address = models.CharField('Address', max_length=120, null=False)
    contact_number = models.IntegerField('Contact Number', null=False)
    email = models.EmailField('Email', null=False)

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'middle_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(FamilyMemberInformation, self).save(*args, **kwargs)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])