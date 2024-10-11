from django import forms
from django.forms import Textarea
from .models import WorkTask, Comments
from django.contrib.auth.models import User


class WorkTaskForm(forms.ModelForm):
    class Meta:
        model = WorkTask
        fields = ('title', 'type', 'description', 'status', 'executor',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows':5})