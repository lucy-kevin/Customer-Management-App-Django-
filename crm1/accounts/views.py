from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/dashboard.html')

def product(request):
    return HttpResponse("Products")

def customer(request):
    return HttpResponse("Customer")
