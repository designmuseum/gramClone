from dataclasses import field
from django import forms

from .models import Image, imgComment


class commentForm(forms.ModelForm):
    comment = forms.CharField(
        label='' ,
        widget=forms.TextInput(attrs={
            'placeholder': 'Add a comment'
        })
       
    )
    class Meta:
        model = imgComment
        fields=['comment']