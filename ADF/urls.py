
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_successful, name='login-view'),
    path('oauth2/', include('django_auth_adfs.urls')),
]
