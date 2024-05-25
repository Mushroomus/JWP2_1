from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config
from zaj3.flaskProject.app import routes, models

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
