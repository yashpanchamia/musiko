from django.urls import path
from . import views

urlpatterns = [
    
    path('news_feed', views.news_feed, name='news')
]