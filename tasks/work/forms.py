from django import forms
from django.forms import Textarea, TextInput
from .models import WorkTask, Comments
from django.contrib.auth.models import User


class WorkTaskForm(forms.ModelForm):     # форма для создания заявки юзером группы Support

    class Meta:
        model = WorkTask
        fields = ['title', 'type', 'description', 'author', 'executor', 'status',]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['title'].widget = TextInput(attrs={'placeholder': 'Адрес'})
            self.fields['description'].widget = Textarea(attrs={'placeholder': 'Описание'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 5, 'placeholder': 'Текст комментария'})
