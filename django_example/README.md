# Django Example Project

##Table of Contents

* [Introduction](#introduction)
* [How to run this example](#how-to-run-this-example)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Project Structure](#project-structure)
* [Implementation Details](#implementation-details)
    * [Project Initialization](#project-initialization)
    * [The Views](#the-views)
    * [The URLs File](#the-urls-file)
    * [Templates](#templates)
    * [If statements](#if-statements)
    * [For Loops](#for-loops)
* [Django ORM](#django-orm)
* [How To Start a Django Project](#how-to-start-a-django-project)
  * [Create Project and App](#create-project-and-app)
  * [Modify settings.py](#modify-settingspy)
  * [Setup Your Database](#setup-your-database)

## Introduction
[Django](https://www.djangoproject.com) is a highly scalable and well known web framework for Python. 
The code in this directory is an example of a simple Django project which uses [yahoo_finance](https://github.com/lukaszbanasiak/yahoo-finance) to fetch stock prices. You can choose between Apple, Microsoft and Google stock. The IBM stock price is updating every 5 seconds.
The second view of this app shows the IBM prices over time as each time a query is performed the result is saved in the database.

Django has a very good [tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/) (also VERY long) which explains everything you need to know about the framework. If you have time or want more detailed information I encourage you to read it. 

## How to run this example
### Prerequisites 
- Make sure you have **virtualenv** and **pip** installed (as described in the main directory).
- Make sure you have MySQL up and running on your machine

### Installation
- Clone this repository 
```bash
git clone https://github.com/lsxliron/Zahn-Center-Hackathon-Starter-Kit.git
```
- `cd` to the `flask_example` directory and run
```bash
pip install -r requirements.txt
```

- Edit the `DATABASES` variable `settings.py` and set the username and password to match you MySQL user.
If you do not want to change it, I will assume that you have MySQL user with username `dev` and password `abcd1234`
- Once the installation is done, open MySQL console and create a new database called `django_example`
```sql
CREATE DATABASE django_example;
```
- cd to `django_example` directory and run the following commands
```bash
# Detect any migrations that occured in the database
python manage.py makemigrations 
# Apply migrations
python manage.py migrate
```
- To run the server run
```bash
python manage.py runserver
```

## Project Structure
```
django_example // root
      |
      |
      |--- django_example // project settings
      |          |
      |          |--- settings.py 
      |          |--- urls.py // project available URLs
      |          |--- wsgi.py // WSGI config
      |
      |--- example // the example app
      |       |
      |       |--- migrations // contains the database migrations
      |       |--- static // static files to serve (e.g js, CSS, images, etc.)
      |       |--- templates
      |       |        |
      |       |        |---example //contains the app HTML files 
      |       |
      |       |--- admin.py //admin database models 
      |       |--- apps.py  // app settings
      |       |--- models.py // the database models
      |       |--- views.py // the app logic
```

## Implementation Details
**Note:** If you read this part I assume you already went over the source code. There are some useful comments there.

### Project Initialization
To start a Django project, you must use the `django-admin` command:
```bash
django-admin startproject project_name
```

this will create a directory called `project_name` with the project settings in it. Django projects are built from apps. An app is a small piece of code that is in charge on one thing and one thing only. This way, you can write many micro services that will integrate into one meaningful thing.

To create an app, you must use the `manage.py` file that the previous command created for you in the `project_name` directory
```bash
python manage.py startapp app_name
```

### The Views
In the new app that we created in the last command, there is a file called `views.py` which will contain all our app logic. 
Notice that the `getAnswer` function returns a `JSON` response. However `getTickerHistory` function return a template with some extra variables. Those variables will be available to us in the HTML file as we will see in the next sections.
The syntax for returning a template is 
```python
return render(request, 'templates/example/template_name.html', {'foo':'bar', 'fiz': 'buz'})
```
The dictionary in the third argument may have complex values like lists and dictionaries. 

### The URLs File
In the project directory there is a file named `urls.py` which is in charge on all the available URLs and their functionality. After adding new views to our `views.py`  file, we have to set a URL for it so it will be available to the users. The URL structure in this file is as follows:
```python
url(r'$^', example_views.index, name='home'),
url(r'^tickerHistory', example_views.getTickerHistory, name='history')
```
The first argument is a [regular expression](https://docs.python.org/2/library/re.html) which should match the URL. The second argument is the name of your function in the `views.py` file and the last argument is the view name. The name argument is important if you want to access it from an HTML form.

### Templates
Django has its own [templating engine](https://docs.djangoproject.com/en/1.10/topics/templates/.) This is useful to perform some logic operations on our backend the return variables to the HTML files. 
The `index` function in `views.py` returns a template called `index.html`.
Note that each app should contain its own `templates` directory. For example
```bash
app_name/templates/app_name/index.html
```

Notice that beside `base.html`, each template in the `example/templates/example` folder, has the following structure:
```html
{% extends "main/base.html" %}

{% block content %}
 ...
{% endblock %}
```

This will take the template `templates/example/base.html` which contains the HTML head and body, and will put the contents of `templates/example/index.html` in the right place. 

If you will take a look on `getTickerHistory` function in `views.py`, you will see that this functions returns a template and some more variables. Those variables can be displayed in the HTML file. You can take a look on `templates/example/history.html`. In short:

#### If statements
```html
{% if foo=="big" %}
    <h1> Big Text </h1>
{% else %}
    <h4> Small Text </h4>
{% endif %}
```

#### For Loops
In the `render_template` function, you can return variables that are lists or dictionaries. You can iterate over them using the following
```html
<label> List example</label>

<ul>
    {%  for name in names %}
        <li> {{ name }} </li>
    {% endfor %}
</ul>

<label> Dictionary example </label>
<dl>
    {% for key, val in dict %}
        <dt> {{ key }} </dt>
        <dd> {{ val }} </dd>
    {% endfor %}
</dl>
```

Notice that control statements are written between `{% stmt %}` and variable names are written as `{{ foo }}`.

## Django ORM
Django has its own [ORM](https://docs.djangoproject.com/en/1.10/topics/db/) in order to interact with the database. Instead of creating SQL tables and perform insert, deletions and update using plain SQL, you can define a model which represents a table using Python. Then, you can perform SQL queries in a Pythonic way.

The `models.py` defines a Ticker object as following
```python
from __future__ import unicode_literals
from django.db import models
import datetime

class Ticker(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
```
You can find more information on Django data types [here](https://docs.djangoproject.com/en/1.10/ref/models/fields/)

The following is a very basic usage
```python
class Foo(db.Model):
    id = models.AutoField(primary_key=True)
    bar = models.CharField(max_length=10)

# Insert
a = Foo(bar='abc')
b = Foo(bar='def')

# Save objects
a.save()
b.save()

# Query
result = Foo.objects.filter(bar='abc')
```

### Django Shell
Django provides us with a useful tool to play and test with our models. when your run `python manage.py shell`, you can import your model class. That way you can create, update and query for objects in your database. This is useful for testing and debugging.

## How To Start a Django Project
### Create Project and App
From the *Project Initialization* section:
>To start a Django project, you must use the `django-admin` command:
```bash
django-admin startproject project_name
```

>this will create a directory called `project_name` with the project settings in it. Django projects are build from apps. An app is a small piece of code that is in charge on one thing and one thing only. This way, you can write many micro services that will integrate into one meaningful thing.

> To create an app, you must use the `manage.py` file that the previous command created for you in the `project_name` directory
```bash
python manage.py startapp app_name
```
>>>

### Modify settings.py
Every app you create using the `startapp` command, should be added to the settings file under the `INSTALLED_APPS` section.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your app here
]
```

### Setup Your Database
Django let you choose which database you want to use (SQLite, MySQL, PostgrSQL). You will need to change the `DATABSES` variable your settings file accordingly. MySQL example:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 
        'NAME': 'example', #Database name
        'USER': 'dev', # Username for MySQL
        'PASSWORD': 'password', # Password for the database
        'HOST': 'localhost' # Database host
    }
}
```

You can find more information about Django backends and configurations in the following links:

- [PostgrSQL](https://docs.djangoproject.com/en/1.10/ref/databases/#postgresql-notes)
- [MySQL](https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-notes)
- [SQLite](https://docs.djangoproject.com/en/1.10/ref/databases/#sqlite-notes)

<hr />
After you made the above changes, you should run the following from your project directory:
```bash
# Detect any migrations that occured in the database
python manage.py makemigrations 
# Apply migrations
python manage.py migrate
```

Now your server should be up and running.

**Do not forget to add new views to the `url.py` file in order to view them on the browser**
