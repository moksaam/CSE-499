from flask import Flask, render_template, request, session, redirect
from functools import wraps
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

# Database
from mydb import uri
client = MongoClient(uri)
db = client.mongologin

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