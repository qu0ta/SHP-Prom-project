
from django.contrib import admin
from django.urls import path, include
from newsfeed import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('news/', include('newsfeed.urls')),
]
