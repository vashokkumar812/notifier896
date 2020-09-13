from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/',views.signin,name='login'),
    path('p/<int:room_name>/', views.room, name='room'),
]