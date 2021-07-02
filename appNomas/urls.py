from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.index ),
    path('login',views.login_user),
    path('form', views.form),
    path('register',views.register),
    path('logout', views.logout),
]
