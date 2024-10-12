from .models import Advert
from django.forms import ModelForm, TextInput, Textarea


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'content']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание'
            }),
        }