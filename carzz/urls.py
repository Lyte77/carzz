from django.urls import path
from. import views

app_name = 'carzz'

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('profile_list/<int:pk>/', views.profile_list, name='profile-list'),
    # path('profile/<int:pk>/',views.profile,name='profile'),
    path('dashboard/<int:dealer_id>/', views.dashboard, name='dashboard'),
    path('set-profile/', views.setup_profile,name='setup_profile'),
    path('update-profile/', views.update_profile,name='update-profile'),
    path('dealer_profile/<int:dealer_id>/', views.dealer_profile,name='dealer_profile'),

    path('car/<int:id>/',views.car_detail_page, name='car_detail'),
    path('add_car/',views.add_car,name='add_car'),
    path('edit-car/<int:id>/',views.edit_car, name='edit-car'),
    path('delete-car/<int:id>/', views.delete_car,name='delete_car'),

]
