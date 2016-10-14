from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt    
from models import Ticker
import json
from yahoo_finance import Share
import ipdb
# Create your views here.

def index(request):
    return render(request, 'example/index.html', {'active':'main'})

@csrf_exempt
def getAnswer(request):
    """
        Returns a JSON object with the price, symbol and name of a share
        The request parameters should be:
            - ticker: the share symbol (str)
            - store: True if we should store the data in the database, false otherwise

        :rtype: dict
    """
    

    if request.method == "OPTIONS": 
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response['Access-Control-Max-Age'] = 1000
        # note that '*' is not valid for Access-Control-Allow-Headers
        response['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
        return response
    
    # Get data from request
    data = json.loads(request.body)
    ticker = data["ticker"]

    # Create share
    share = Share(ticker)

    # Get share price as a string
    price = "{} {}".format(share.get_price(), share.data_set["Currency"])

    # Insert price and timestamp to the database if store==True
    if data["store"]:
        # Create a ticker object
        t = Ticker(price=float(share.get_price()), symbol=ticker)
        # Try to save in the database or print an error
        try:
            t.save()
       
        except Exception as e:
            print e

    return JsonResponse({"price": price, "name": share.data_set["Name"]})

def getTickerHistory(request):
    """
        Returns the history view
    """
    # Get all the data from the database
    tickers_objects = Ticker.objects.all()

    # Serialize the data
    tickers = [t.serialize() for t in tickers_objects]
    return render(request, "example/history.html", {'tickers':tickers, 'active':'history'}) 