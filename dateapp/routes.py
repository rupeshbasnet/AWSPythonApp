from . import app
import datetime
from flask import request
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		day = request.form["userinput"]
		dateTime = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%A')
		outputMonth = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%B')
		outputYear = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%Y')
		outputDate = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%d')
		return render_template('index.html', day = dateTime, date = outputDate, month = outputMonth,
								year = outputYear)
	if request.method == 'GET':
		return render_template('index.html')
