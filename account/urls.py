from django.urls import path
from .views import RegisterView,LoginView,CustomLogoutView,HomeView
urlpatterns = [
    path('',HomeView,name='home'), 
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', CustomLogoutView, name='logout'),
]