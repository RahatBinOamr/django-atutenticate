from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def HomeView(request):
  return render(request,'home.html')


def RegisterView(request, *args, **kwargs):
  if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     password = request.POST.get('password')
     user = User.objects.create_user(username=name, email=email, password=password)
     user.save()
     return redirect('login')
  return render(request,'register.html')

def LoginView(request, *args, **kwargs):
  if request.method == 'POST':
    name = request.POST.get('name')
    password = request.POST.get('password')
    user = authenticate(username = name, password = password)
    if user is not None:
       login(request, user)
       return redirect('home')
  return render(request,'login.html')

def CustomLogoutView(request, *args, **kwargs):
  logout(request)
  return redirect('login')