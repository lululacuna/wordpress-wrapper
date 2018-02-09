from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object('config')
# Temporary database while app is in development/testing.
# Switch to more secure database outside of app when in
# production.
db = create_engine('sqlite:///users.db')
Base = declarative_base()

from app import views, models