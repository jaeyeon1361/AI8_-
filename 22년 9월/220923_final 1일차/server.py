from distutils.log import debug
from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index() :
    return 'Index page'

@app.hello('/')
def index() :
    return 'Hello page'


app.run(debug=True) # 5000port를 이용하고, 새로고침하면 반영