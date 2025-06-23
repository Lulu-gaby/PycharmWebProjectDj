from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('facts',views.facts, name='page2'),
    path('recipies', views.recipies, name='page3'),
    path('photos', views.photos, name='page4'),
    path('stories', views.stories, name='page5')
]
