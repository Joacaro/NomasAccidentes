from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.index ),
    path('login',views.login_user),
    path('solicitar', views.solicitar),
    path('register',views.register),
    path('logout', views.logout),
]
