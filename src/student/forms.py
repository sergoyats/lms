from django.forms import ModelForm
from django.core.exceptions import ValidationError

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):
    pass


class StudentEditForm(StudentBaseForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.all().filter(email=email).exists():
            raise ValidationError('This email exists, create a unique one.')
        return email

    def clean(self):
        name = self.cleaned_data
        if name['first_name'] == name['last_name']:
            raise ValidationError('First and last names are the same! This is unacceptable!')
        return name


class StudentDeleteForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = []
