from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///akademik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(50), nullable= False)
    name = db.Column(db.String(50),  nullable= False)
    address = db.Column(db.String(256), nullable= False)
    email = db.Column(db.String(50), nullable= False)

db.create_all()