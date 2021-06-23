from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from validate_email import validate_email
from django.http import request
from django.contrib import auth

class Student_register(View):
    def get(self, request):
        return render(request, 'users/student_register.html')
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if password!=password2:
            messages.error(request, 'password does not match')
            return render(request, 'users/student_register.html', context)
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request, 'password too short')
                    return render(request, 'users/student_register.html', context)
                user = User.objects.create_user(username=username, email=email,password=password)
                usertype=Student.objects.create(user=user)
                usertype.save()
                user.save()
                
                return render(request, 'users/login.html')
            messages.error(request, 'email already exists')
        messages.error(request,'user already exists')
        return redirect('login')

class Company_register(View):
    def get(self, request):
        return render(request, 'users/company_register.html')
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if password!=password2:
            messages.error(request, 'password does not match')
            return render(request, 'users/company_register.html', context)
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request, 'password too short')
                    return render(request, 'users/company_register.html', context)
                user = User.objects.create_user(username=username, email=email)
                usertype=Company.objects.create(user=user)
                usertype.save()
                user.set_password(password)
                user.save()
               
                return render(request, 'users/login.html')
            messages.error(request, 'email already exists')
        messages.error(request,'user already exists')
        return render( request, 'users/company_register.html')

   
class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            print(username)
            print(password)
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user :
                auth.login(request, user)
                messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                return redirect('home')


        messages.error(
        request, 'Please fill all fields')
        return render(request, 'users/login.html')

def home(request):
    return render(request,'users/home.html')
    