from flask import render_template_string
from WebService import app

@app.route('/')
def home_page():
    return "Hello world"