from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MonthlyRegistration
from .models import MonthlyTransaction
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View
from django.urls import reverse

from django.template.loader import get_template

# Create your views here.


def home(request):
	
	return render(request,"index.html")

