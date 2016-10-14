from flask import render_template, Blueprint, request, jsonify
from yahoo_finance import Share
from app import db
from app.models import Ticker


example_blueprint = Blueprint(__name__, "example")

@example_blueprint.route("/", methods=["GET"])


def index():
    """
        Returns the homepage view
    """
    return render_template("example/index.html", active="main")


@example_blueprint.route("/answer", methods=["POST"])
def getAnswer():
    """
        Returns a JSON object with the price, symbol and name of a share
        The request parameters should be:
            - ticker: the share symbol (str)
            - store: True if we should store the data in the database, false otherwise

        :rtype: dict
    """

    # Get data from request
    data = request.get_json()
    ticker = data["ticker"]

    # Create share
    share = Share(ticker)

    # Get share price as a string
    price = "{} {}".format(share.get_price(), share.data_set["Currency"])

    # Insert price and timestamp to the database if store==True
    if data["store"]:
        # Create a ticker object
        t = Ticker(float(share.get_price()), ticker)
    
        # Try to save in the database or print an error
        try:
            db.session.add(t)
            db.session.commit()
            db.session.flush()
        except Exception as e:
            print e
            db.session.rollback()

    return jsonify({"price": price, "name": share.data_set["Name"]})



@example_blueprint.route("/tickerHistory", methods=["GET"])
def getTickerHistory():
    """
        Returns the history view
    """
    # Get all the data from the database
    tickers_objects = Ticker.query.all()

    # Serialize the data
    tickers = [t.serialize() for t in tickers_objects]
    return render_template("example/history.html", tickers=tickers, active="history") 