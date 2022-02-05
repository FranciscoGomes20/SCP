from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('icons', views.icons, name='icons'),
    path('map', views.map, name='map'),
    path('notifications', views.notifications, name='notifications'),
    path('user', views.user, name='user'),
    path('tables', views.tables, name='tables'),
    path('typography', views.typography, name='typography'),
    path('rtl', views.rtl, name='rtl'),
    path('upgrade', views.upgrade, name='upgrade'),
]