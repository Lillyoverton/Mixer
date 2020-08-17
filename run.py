from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

INGREDIENTSDB = 'ingredients.db'

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/accessdenied')
def accessdenied():
    return render_template ('accessdenied.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/ingredients')
def ingredients():
    con = sqlite3.connect(INGREDIENTSDB)

    spirits = []
    cur = con.execute('SELECT spirit FROM spirits')
    for row in cur:
        spirits.append(list(row))

    return render_template ('ingredients.html',
                            spirits=spirits)

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')
