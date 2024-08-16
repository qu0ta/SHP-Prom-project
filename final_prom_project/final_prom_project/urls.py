
from django.contrib import admin
from django.urls import path
from newsfeed import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
]
