from app import db
import datetime

class Ticker(db.Model):
    """
        This class represents share basic data
    """

    # Specify table name
    __tablename__ = "ticker"

    # Attributes
    id = db.Column(db.Integer, autoincrement=True, nullable=False, unique=True)
    symbol = db.Column(db.String(length=10), nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)
    price = db.Column(db.Float(precision=4), nullable=False)

    # Specify primary key
    db.PrimaryKeyConstraint(id)


    # Constuctor
    def __init__(self, price, symbol):
        """
            Creates a new Ticker object
            :param price: The stock price
            :param symbol: The stock symbol (ticker)
            :type price: float
            :type symbol: str
        """
        self.price = price
        self.symbol = symbol
        self.timestamp = datetime.datetime.now()

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