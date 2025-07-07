from django.urls import path
from . import views

urlpatterns = [
    path('', views.films, name='home'),
    path('add/', views.add_films, name='add_films'),

]