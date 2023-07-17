from flask import render_template, request
from dashboard import app
from dashboard.dbcontroller import DBController

@app.route('/')
def home():
    DBController.test_operation()
    return "Hello World!"