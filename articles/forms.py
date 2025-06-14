from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumbnail']
        labels = {
            'title': 'Title',
            'body': 'Text',
            'thumbnail': 'Thumbnail'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter article title', 'class': 'form-control mb-3'}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter article text', 'class': 'form-control mb-3'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}),
        }
