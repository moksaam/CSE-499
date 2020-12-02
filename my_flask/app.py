from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from pymongo import MongoClient
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

# Database
#app.config["MONGO_URI"] = "mongodb+srv://test_user:testasNM0103!@cluster0.kkkfb.mongodb.net/test?retryWrites=true&w=majority"	
uri = "mongodb+srv://test_user:testasNM0103%21@cluster0.kkkfb.mongodb.net/mongologin?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.mongologin

#mongo = PyMongo(app)

# Decorators
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect('/')
	return wrap

# Routes
from user import routes
from character import routes

@app.route('/')
def home():
	return render_template('home.html')	  # render a template


@app.route('/register')
def register():
	return render_template('register.html')  # render a template


@app.route('/index/')
def index():
	return render_template('index.html')  # render a template


@app.route('/createChar')
def createChar():
	return render_template('createChar.html')  # render a template


@app.route('/charSkills')
def charSkills():
	return render_template('charSkills.html')  # render a template


@app.route('/charSpells')
def charSpells():
	return render_template('charSpells.html')  # render a template


@app.route('/equipment')
def equipment():
	return render_template('equipment.html')  # render a template