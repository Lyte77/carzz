from django.urls import path
from. import views

app_name = 'carzz'

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('create-profile/', views.create_dealer_profile, name='dealer-profile'),
    path('profile/<int:id>/', views.profile_page, name='profile'),
    path('edit/', views.edit_profile,name='edit'),
]
