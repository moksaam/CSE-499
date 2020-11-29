from flask import Flask
from flask import flash, redirect, render_template, requests, session, abort
import os

app = Flask(__name__)
def createCharSubmit():
	
	pass
@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello Boss!"


@app.route('home/login', methods=['POST'])
def do_admin_login():
	if requests.form['password'] == 'password' and requests.form['username'] == 'admin':
		session['logged_in'] = True
		return redirect('/index')
	else:
		flash('wrong password!')
		return home()


@app.route('home/index')
def index():
	if session.get('logged_in'):
		return render_template('index.html')
	else:
		return "Hello Boss!"
	


@app.route('charSheet/createChar', methods=['POST'])
def createChar():
	return render_template('createChar.html')  # render a template


@app.route('charSheet/charSkills')
def charSkills():
	return render_template('charSkills.html')  # render a template


@app.route('charSheet/charSpells')
def charSpells():
	return render_template('charSpells.html')  # render a template


@app.route('charSheet/equipment')
def equipment():
	return render_template('equipment.html')  # render a template


@app.route('/test')
def test():

	POST_USERNAME = "python"
	POST_PASSWORD = "python"

	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
	result = query.first()
	if result:
		return "Object found"
	else:
		return "Object not found " + POST_USERNAME + " " + POST_PASSWORD


@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()
	if __name__ == "__main__":
		app.secret_key = os.urandom(12)
		app.run(debug=True, host='0.0.0.0', port=4000)