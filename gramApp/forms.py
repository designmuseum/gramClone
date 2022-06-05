from dataclasses import field
from django import forms

from .models import Image, imgComment




# class newPostForm(forms.ModelForm):
#     image = forms.ImageField(required=True)
#     caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
#     class Meta:
#         model = Image
#         fields=['image', 'caption']


class commentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder': 'Comment'
        })
    )
    class Meta:
        model = imgComment
        fields=['comment']