from django import forms

from app1.models import *

class Creation(forms.ModelForm):
    class Meta:
        model=Question
        fields='__all__'
        