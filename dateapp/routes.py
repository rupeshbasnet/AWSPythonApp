from . import app
import datetime
from flask import request
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		day = request.form["userinput"]
		print (day)
	return render_template('index.html', day = day)
