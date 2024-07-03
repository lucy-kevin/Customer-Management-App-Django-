# URL Routing
We are going to learn how URLs and views work together to return templated to the users.

when ever the user types in the URL path, it is the urls.py file to find the partern the user typed in the browser and return the back page
### urls.py file under the project directory
```python
#urls.py file under the project folder


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    
   
]

```

### Create a urls.py file under the app folder

```python
    from django.urls import path
from . import view
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
   
]
```


### Update the views.py file
```python
    from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def product(request):
    return HttpResponse("Products")

def customer(request):
    return HttpResponse("Customer")
```

Run it and you will be able to view the home page
when you change the url to http://127.0.0.1:8000/products/ products webpage will be displayed.