
class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'M^3lfDmx@EXEmqVW0D@67GkcBLzg30G69pZ!Hb#5W0N25Bb@<y.5SvG#s2rX@Xbuh>$miT3<X'
    STATIC_FOLDER = 'static'
    
    # Connection string for the databse.
    # Structure:: mysql://username:password:host/db_name
    SQLALCHEMY_DATABASE_URI = "mysql://dev:abcd1234@localhost/flask_boilerplate"