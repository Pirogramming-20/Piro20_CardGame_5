from django.urls import path
from .views import *

app_name='users'

urlpatterns = [
    path("",main,name='main'),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
    path("ranking/", ranking, name="ranking"),
    path("set_name/", set_name, name="setname"),
    path('delete/<int:pk>/', delete, name ='delete'),
    path('update/<int:pk>/', update, name ='update'),
    #path('detail/<int:pk>/', detail, name='detail'),
]