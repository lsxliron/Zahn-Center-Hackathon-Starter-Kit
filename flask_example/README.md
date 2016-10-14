# Flask Example Project

## Table of Contents

* [Introduction](#introduction)
* [How to run this example](#how-to-run-this-example)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Project Structure](#project-structure)
* [Implementation Details](#implementation-details)
  * [Project Initialization](#project-initialization)
  * [The Views](#the-views)
  * [Routes](#routes)
  * [Templates](#templates)
    * [If statements](#if-statements)
    * [For Loops](#for-loops)
* [SQLALCHEMY](#sqlalchemy)


## Introduction
The code in this directory is an example of a simple flask web server which uses [yahoo_finance](https://github.com/lukaszbanasiak/yahoo-finance) to fetch stock prices. You can choose between Apple, Microsoft and Google stock. The IBM stock price is updating every 5 seconds.
The second view of this app shows the IBM prices over time as each time a query is performed the result is saved in the database.

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
- Once the installation is done, open MySQL console and create a new database called `flask_example`
```sql
CREATE DATABASE flask_example;
```
- Edit the `SQLALCHEMY_DATABASE_URI` in `config.py` file. This is the *connection string* to the database. When using MySQL it has the following structure
```
mysql://username:password@host/dbname
```
If you do not want to change it, I will assume that you have MySQL user with username `dev` and password `abcd1234`

- From the `flask_example` directory, run the following command in order to create the necessary tables in in your database
```bash
python syncdb.py
```
- Run the following command in order to start the server
```bash
python runserver.py
```
- Open your browser and navigate to `http://localhost:5500`


## Project Structure
Flask has a very concise structure. This project is built as following
```
flask_example  //root directory
    |
    |--- app //All our project files are in this directory
    |     |
    |     |--- example 
    |     |       |
    |     |       |--- __init__.py // Python initialization file
    |     |       |-- views.py //contains the logic of the app
    |     |       
    |     |--- static // contains static files we want to serve such as
    |     |           // scripts, CSS, images, etc.
    |     |       
    |     |--- templates // contains the app HTML files
    |     |       
    |     |--- models.py // Contains our models
    |
    |--- config.py // app configuration
    |--- runserver.py // a script to start the server
    |--- syncdb.py // a script to create the tables in the database
```

## Implementation Details
**Note:** If you read this part I assume you already went over the source code. There are some useful comments there.

### Project Initialization
The `__init__` file contains the code that initialize the project. Make sure you read it since it is well documented and explains how to connect the app to your database.

For your own convenience, create a `runserver.py` file in the root directory of the project with the following code
```python
from app import app
app.run(debug=True, host='0.0.0.0', port=5000)
```

This will allow you to update your `__init__.py` file while the app is running and will also resolve many path issues. Of course, you can change the function arguments as you want. 

### The Views
This file contains the project logic. Notice that flask uses *Blueprints*. 
```python
example_blueprint = Blueprint(__name__, "example")
```

A Blueprint is a small piece of logic that does something. You can create a project from several blueprints. For example, If your project has an API and a user management system, you can have a blueprint for each. This approach helps to keep your code short.

### Routes
Notice that each function in `views.py` starts with following line
```python
@example_blueprint.route("/", methods=["GET"])
```
This creates a *Route* to a function. Meaning, when the user will navigate to `www.example.com`, he will get to the route that in charge of `/`. 
When you create a Route, you need to define which methods the browser can user (GET, POST, etc.)

### Templates
Flask uses [Jinja2](http://jinja.pocoo.org) templating engine. This is useful to perform some logic operations on our backend the return variables to the HTML files. 
The `index` function in `views.py` returns a template called `index.html`.

Notice that each template in the `templates/example` folder, has the following structure:
```
{% extends "main/base.html" %}

{% block content %}
 ...
{% endblock %}
```

This will take the template `templates/main/base.html` which contains the HTML head and body, and will put the contents of `templates/example/index.html` in the right place. 

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

## SQLALCHEMY
[SQLAlchemy](http://www.sqlalchemy.org) is the most common ORM for python. If you will use it correctly, it will make your life easier. 

Instead of creating SQL tables and perform insertions, deletions and updates using plain SQL, you can define a model which represents a table using Python. Then, you can perform SQL queries in a Pythonic way. 

The `models.py` defines a Ticker object as following
```python

class Ticker(db.Model):
    id = db.Column(db.Integer, autoincrement=True, nullable=False, unique=True)
    symbol = db.Column(db.String(length=10), nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)
    price = db.Column(db.Float(precision=4), nullable=False)

    db.PrimaryKeyConstraint(id)
```

You can find more information on SQLAlchemy data types and their arguments [here](http://docs.sqlalchemy.org/en/latest/core/type_basics.html)

The following is a very basic usage of SQLAlchemy
```python

from app import db

# Define a model
class Foo(db.Model):
    id = db.Column(db.Integer, autoincrement=True, nullable=False, unique=True)
    bar = db.Column(db.String(length=10))

    def __init__(self, bar):
        self.bar = bar


# Insert
a = Foo('abc')
b = Foo('def')
db.session.add(a)
db.session.add(b)
db.commit()

# Query
result = Foo.query.filter_by(bar='abc')
```