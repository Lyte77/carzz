"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from django.urls import path, include

urlpatterns = [
   
    path('theboss/', admin.site.urls),
    
    path('__reload__/', include("django_browser_reload.urls")),
    path('account/',include('account.urls')),
    path('accounts/', include('allauth.urls')),
    # path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('carzz.urls', namespace='carzz')),
    # path('api/', include('carzz_api.urls')),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')), 
   
    


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.ENVIRONMENT == 'development':
    urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )

 