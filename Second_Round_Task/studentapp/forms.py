from django import forms
from django.db.models import fields
from .models import Studentinfo,StudentAcademics

class StudentInfoForm(forms.ModelForm):

    class Meta:
        model = Studentinfo
        fields = '__all__'

class StudentAcademicsForm(forms.ModelForm):
    class Meta:
        model = StudentAcademics
        fields = ('math','physics','chemistry','biology','english')



