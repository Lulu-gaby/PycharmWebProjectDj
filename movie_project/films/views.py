from django.shortcuts import render, redirect
from .models import Films_post
from .forms import FilmsForm


def films(request):
    films = Films_post.objects.all().order_by('-date')
    return render(request, 'films/films.html', {'films': films})

def add_films(request):
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FilmsForm()
    return render(request, 'films/add_films.html', {'form': form})