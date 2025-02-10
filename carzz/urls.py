from django.urls import path
from. import views

app_name = 'carzz'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('coming-soon/', views.coming_soon_page,name='coming-soon'),
    # path('profile_list/<int:pk>/', views.profile_list, name='profile-list'),
    # path('profile/<int:pk>/',views.profile,name='profile'),
    path('dashboard/', views.dashboard_router, name='dashboard_router'),
    path('dealer/dashboard/<int:dealer_id>/', views.dealer_dashboard, name='dealer_dashboard'),
    path('user/dashboard/<int:user_id>/', views.user_dashboard, name='user_dashboard'),

    
    path('create-profile/dealer/', views.create_profile,name='create_profile'),
    path('create-profile/user/', views.create_user_profile,name='create_user_profile'),

    
    # path('update-profile/dealer/', views.update_profile,name='update-profile'),
    # path('update-profile/user/', views.update_user_profile,name='update_user_profile'),
    path('dealer_profile/<int:dealer_id>/', views.dealer_profile,name='dealer_profile'),
    path('user_profile/<int:user_id>/', views.user_profile,name='user_profile'),
    path('dealer/update/',views.update_dealer_profile,name='update_dealer_profile'),
    path('user/update/',views.update_user_profile,name='update_user_profile'),
    path('profile/verify-email/',views.profile_verify_email, name="profile-verify-email"),

    path('car/<int:id>/',views.car_detail_page, name='car_detail'),
    path('all-cars/',views.car_page, name='car_page'),
    path('add_car/',views.add_car,name='add_car'),
    path('edit-car/<int:id>/',views.edit_car, name='edit-car'),
    path('delete-car/<int:id>/', views.delete_car,name='delete_car'),
    path('save-car/<int:car_id>/', views.save_car,name='save_car'),
    path('delete_saved_car/<int:car_id>/', views.delete_saved_car,name='delete_saved_car'),
    # path('cloudinary_test/', views.cloudinary_test_view, name='cloudinary_test'),

]
