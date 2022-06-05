from django import forms

from .models import Image




class newPostForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    class Meta:
        model = Image
        fields=['image', 'caption']