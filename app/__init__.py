from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initialise flask
app = Flask(__name__)


#set configurations 
app.config.from_object(DevConfig)

#intitialize flask extensions
bootstrap = Bootstrap(app)

from app import views
from app import errors