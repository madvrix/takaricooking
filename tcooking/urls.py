from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'tcooking'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('<id>detail', views.detail),
    path('<id>favorit', views.favor),
    path('<id>favoritrc', views.favorc),
    path('<id>detailrekomen', views.detailrekomen),
    path('menu', views.menu, name='menu'),
    path('profil', views.profil, name='profil'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
]