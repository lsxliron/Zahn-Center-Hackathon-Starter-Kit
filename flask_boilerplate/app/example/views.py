from flask import render_template, Blueprint
from app import db
# Import models after you wrote them
# from app.models import Foo


example_blueprint = Blueprint(__name__, 'example')

@example_blueprint.route('/', methods=['GET'])
def index():
    return render_template('example/index.html', msg="Hello From Flask!")