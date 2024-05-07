"""
URL configuration for trakky_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.urls import include

from register import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #REST FRAMEWORK URLS
    path('api/', include('products_and_meals.api.urls', 'products_and_meals_api')),
    #USER_AUTH URLS
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='register'),
    path('test_token/', views.test_token, name='test_token')

]
