from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Films_post

class FilmsForm(ModelForm):
    class Meta:
        model = Films_post
        fields = ['title', 'description', 'comments', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control','placeholder':'Название фильма'}),
            'description': Textarea(attrs={'class': 'form-control','placeholder':'Описание фильма'}),
            'comments': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзывы о фильме'}),
            'date': DateTimeInput(attrs={'type': 'datetime-local'})
        }