
from flask import Flask, render_template, redirect, request, session, flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
	def process_registration():
	  email = request.form['email']
	  first_name = request.form['name']
	  last_name = request.form['last']
	  password = request.form['password']
	  confirm_password = request.form['confirm']
	  validation = True
	  if len(first_name)<1 or len(last_name)<1:
	      flash("First name and last name cannot be empty")
	      validation = False

	  if len(email)<1:
	      flash("Email cannot be empty")
	      validation = False
	  elif not EMAIL_REGEX.match(email):
	      flash("Invalid Email Address!")

	  if len(password) < 8:
	      flash("Password must be at least 8 characters")
	      validation = False
	  elif not PASSWORD_REGEX.match(password):
	      flash("Password must contain at least 1 uppercase, 1 lowercase, and 1 numeric characters")
	      validation = False

	  if password != confirm_password:
	      flash("Passwords don't match")
	      validation = False

	  if not validation:
	      return render_template("registration.html", email=email, first_name=first_name, last_name=last_name)
	  return render_template("success.html")
app.run(debug=True)
