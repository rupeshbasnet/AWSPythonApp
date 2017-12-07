from . import app
import datetime
from flask import request
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		day = request.form["userinput"]
		dateTime = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%A')
		return render_template('index.html', date = dateTime)
	if request.method == 'GET':
		return render_template('index.html')
