from django.shortcuts import render, redirect
from .models import News_post
from .forms import NewsForm
from django.contrib.auth.decorators import login_required

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('news_home')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})