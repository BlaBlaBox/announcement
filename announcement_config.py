import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

url = os.getenv("DATABASE_URL")
if url is None:
    url = os.getenv("DATABASE_URL_ANNO")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# "postgres://ugqnlwoepinknu:15d498d0272fd7fb011c3cf2687c2910258ba7527ed93d8abb7de7b04b31aa22@ec2-54-247-125-116.eu-west-1.compute.amazonaws.com:5432/d39kutv9dfcmb1"
