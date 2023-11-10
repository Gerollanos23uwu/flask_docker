from flask import(
    Flask,
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from dotenv import load_dotenv
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://BD2021:BD2021itec@143.198.156.171:3306/blog1'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')


db = SQLAlchemy(app=app)
migrate = Migrate(app,db)
ma = Marshmallow(app)

load_dotenv()

from app.views import view