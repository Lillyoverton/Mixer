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

    wines = []
    cur = con.execute('SELECT wine FROM wines')
    for row in cur:
        wines.append(list(row))

    mixers = []
    cur = con.execute('SELECT mixer FROM mixers')
    for row in cur:
        mixers.append(list(row))

    freshstuff = []
    cur = con.execute('SELECT fresh FROM freshstuff')
    for row in cur:
        freshstuff.append(list(row))

    others = []
    cur = con.execute('SELECT other FROM others')
    for row in cur:
        others.append(list(row))

    return render_template ('ingredients.html',
                            spirits=spirits,
                            wines=wines,
                            mixers=mixers,
                            freshstuff=freshstuff,
                            others=others
                            )

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')
