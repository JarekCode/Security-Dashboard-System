from flask import render_template, request
from dashboard import app

@app.route('/')
def home():
    return "Hello World!"