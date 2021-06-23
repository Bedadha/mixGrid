from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
      path('student', Student_register.as_view(), name = 'student'),
      path('company', Company_register.as_view(), name = 'company'),
      path('login', LoginView.as_view(), name = 'login'),
      path('home',views.home,name='home'),

      
]