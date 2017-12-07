from . import app
import datetime
from flask import request
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')
