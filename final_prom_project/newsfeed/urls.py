from django.urls import path
from . import views


urlpatterns = [
    path('all', views.all_news_view, name='all_news'),
]
