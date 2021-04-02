from django.urls import path

from . import views as api_views


urlpatterns = [
    path('v1/register', api_views.registerUser.as_view(), name='register'),
    path('v1/login', api_views.loginUser.as_view(), name='login'),
]
