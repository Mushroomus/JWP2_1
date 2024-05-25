from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config
from zaj3.zad1.app import routes, models

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
