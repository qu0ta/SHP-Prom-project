from django.contrib import admin
from django.urls import path, include
from newsfeed import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home_view, name='home'),
	path('about/', views.about_view, name='about'),
	path('news/', include('newsfeed.urls')),
	path('registration/', views.registration_view, name='reg'),
	path('login/', views.login_view, name='login'),
	path('profile/', views.profile_view, name='profile'),
	path('logout/', views.logout_view, name='logout')

]
