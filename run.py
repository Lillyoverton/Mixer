from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

INGREDIENTSDB = 'ingredients.db'
DRINKSDB = 'drinks.db'

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

@app.route('/drinks', methods=['POST'])
def drinks():
    req_ing = []

    for ingredient in request.form:
        req_ing.append(ingredient)

    con = sqlite3.connect('drinks.db')

    drinks = []

    cur = con.execute('SELECT * FROM drinks')

    matches = []

    for req in req_ing:

        for row in cur:

            for ing in row[3].split(','):
                if req == ing:
                    matches.append(list(row))

    for match in matches:
        match[3] = match[3].split(',')

    con.close()

    return render_template ('drinks.html', matches=matches)
