from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

# Create the main app
app = Flask(__name__)

# Handles Cross Origin Request Security, should be removed in production
CORS(app, resources={r'/*': {'origins': '*', 'headers': ['Content-Type']}})

# Config the app from config.py
app.config.from_object('config.BaseConfig')

# Create the database
db = SQLAlchemy(app)

# Register our example app
from app.example.views import example_blueprint
app.register_blueprint(example_blueprint)

# Import models
from app.models import Ticker



