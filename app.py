import os
from flask import Flask , render_template, url_for, request, redirect
# import csv


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')



