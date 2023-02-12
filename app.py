import os
import pandas as pd
import datetime as dt
import jsons
import json
from flask import Flask , render_template, url_for, request, redirect
# import csv


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/restapi")
def restapi():
    all_jsons = pd.read_json(r'all_folders.json' )
    all_jsons_html = all_jsons.to_html()
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
            Tu będzie strona do pobierania jsonow <br>
            {now}
            {all_jsons_html}
            
"""

