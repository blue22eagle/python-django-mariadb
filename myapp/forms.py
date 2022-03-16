#from django.forms import fields
from django import forms
from myapp.models import myTable

class myTableForm(forms.ModelForm):
    class Meta:
        model= myTable
        fields= '__all__'