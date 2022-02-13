from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.loginUser, name='login'),
    path('icons', views.icons, name='icons'),
    path('map', views.map, name='map'),
    path('notifications', views.notifications, name='notifications'),
    path('user', views.user, name='user'),
    path('typography', views.typography, name='typography'),
    path('register-tickets', views.register_tickets, name='register-tickets'),
]