from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import News_post

class NewsForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control','placeholder':'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control','placeholder':'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
            'pub_date': DateTimeInput(attrs={'type': 'datetime-local'})
        }