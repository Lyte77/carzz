from django.urls import path
from. import views

app_name = 'carzz'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('profile_list/', views.profile_page, name='profile-list'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('set-profile/', views.setup_profile,name='setup_profile'),
    path('update-profile/', views.update_profile,name='update-profile'),


]
