# Customer-Management-App-Django-
I have always wanted to learn API development, I have chosen Django because of a project I am working on with a team of friends under CodePlay

S
## Step 1

Open the the directory in which you are going to be working from make sure your have python installed and then open the terminal and run

```pwsh
pip install django
```
To ensure that Django is installed correctly run
```pwsh
django-admin
```
and a list of subcommands will be displayed.

## Step 2
From the same directory in the terminal we are working from run
```
 django-admin <projectName>

```
Replace `<projectName>` with the name of your project

#### Overview on the files created in the project folder we have just created

- **manage.py:** We never have to touch that file, it gives us access to a list of command we are going to use
- **wsgi.py:** It is a web server django sets up for us, we also dont have to touch it for now
- **urls.py:** Url routing system. We will add a list of paths here.
- **Setting.py** This is the main file we are going to be using.

## Step 3
Lets launch our Django App and see what happens when it runs 
to run it go to the project you created
```pwsh
 cd <projectName>
```
And to launch it run
```pwsh
python manage.py runserver
```
Give it some time and then Open your browser and  see your project on port http://127.0.0.1:8000/
## Step 4
Lets now create our app 
```pwsh
python manage.py startapp <appName>
```
under the app, the main files we will set our emphasis on are:
- **admin.py** file for setting up the admin panel 
- **model.py** where we will build our database and class-based objects and it will represent the file structure we're gonna have in the database
- **veiws.py** the functions or classes that activate the URL patterns go to and trigger to render out a template and so on

## Step 5
Configure our App, so that our project can be connected to the App we do this by adding `appName` to the **settings.py** file in the project folder under the:
```python
INSTALLED_APPS = [
    ...
    'appName',
]