from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentDetail
from Student.forms import CustomerFilterForm,CreateUserForm
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse




# Create your views here.
def home(request):
	
    return render(request,"index.html")


	
