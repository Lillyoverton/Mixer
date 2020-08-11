from flask import Flask, render_template

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
