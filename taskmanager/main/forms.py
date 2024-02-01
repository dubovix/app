from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task" ]
        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Input your name'
                }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input your comment'
            }),

        }


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs = {'placeholder':'Input your name','class':'form-control'}
        )
    )

    email = forms.EmailField(
        min_length=2,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Input your email address','class':'form-control'}
        )
    )

    message = forms.CharField(
        min_length=2,
        widget=forms.Textarea(
            attrs={'placeholder': 'Input your message', 'cols':30, 'rows':9, 'class':'form-control'}
        )
    )