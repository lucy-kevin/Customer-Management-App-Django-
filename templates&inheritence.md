# Creating Templates and inheritence

## step 1
create a folder under your `app` folder called `templates` make sure you are using the correct spelling because it is what django will look for. 
Under `templates` create a folder called `accounts` you can name it the name of the app.

Then go on and create a `dashboard.html` file under `accounts`.
Write some html code there such as 
```html
    <!DOCTYPE html>
<html>
    <head>
        <title>CRM</title>
    </head>
    <body>
        <h1>Dashboard</h1>
    </body>
</html>
```

## Step 2
Update the `views.py` file to
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/dashboard.html')
    #We have updated this line of code so that django locates and displays the dashboard as the home page.
    # Here we are returning a template.

def product(request):
    return HttpResponse("Products")#these are http response

def customer(request):
    return HttpResponse("Customer")

```

Lets now update all of the pages to templetes.

## Templete inheritence

Let us start by creating the parent file `main.html`

```html
    <!DOCTYPE html>
<html>
    <head>
        <title>CRM</title>
    </head>
    <body>

        <h1>Navbar</h1>
        <hr>
        {% block content%} 
        
        
        
        
        {% endblock %}
        <hr>
        <h5>Our footer</h5>
    </body>
</html>


```

and then update the other files
this is file dashboard.html
```html
    {% extends "accounts/main.html" %}

{% block content %}

<h1>Dashboard</h1>

{% endblock %}

```

Update the rest of the files

