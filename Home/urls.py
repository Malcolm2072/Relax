from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="Home",),
    path('register/', views.register, name="Register"),
    path('login/', views.log, name="Login"),
]
