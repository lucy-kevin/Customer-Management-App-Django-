from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def product(request):
    return HttpResponse("Products")

def customer(request):
    return HttpResponse("Customer")