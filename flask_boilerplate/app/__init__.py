from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Create the app
app = Flask(__name__)

# Resolve CORS
CORS(app, resources={r'/*': {'origins': '*', 'headers': ['Content-Type']}})

# Config app
app.config.from_object('config.BaseConfig')

# Create the database
db = SQLAlchemy(app)

from app.example.views import example_blueprint
app.register_blueprint(example_blueprint)



# Import models after you wrote them
# from app.models import Foo