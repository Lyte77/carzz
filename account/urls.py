from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign_up/', views.register_user, name='register')
]
