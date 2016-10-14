from __future__ import unicode_literals
from django.db import models
import datetime

class Ticker(models.Model):
    """
        This class represents share basic data
    """

    # Attributes
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)

    
    def getTimestampString(self):
        """
            Return a timestamp in day/month/year hour:minutes:seconds format
            :rtype: str 
        """
        return self.timestamp.strftime('%m/%d/%Y %H:%M:%S')
        

    def serialize(self):
        """
            Return a serializable ticker object
            :rtype: dict
        """
        return {
            "symbol": self.symbol,
            "price": self.price,
            "timestamp": self.getTimestampString()
        }