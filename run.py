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

    requested_ingredients = request.form

    con = sqlite3.connect('drinks.db')

    cur = con.execute('SELECT * FROM drinks')

    all_drinks = []

    for row in cur:
        all_drinks.append(list(row))
    con.close()

    matches = []

    for drink in all_drinks:
        drink_ingredients = drink[3].split(',')

        if set(requested_ingredients) < set (drink_ingredients):
            matches.append(drink)

            print(matches)

        else: print('no matches found')

    for match in matches:
        match[3] = match[3].split(',')


    return render_template ('drinks.html', matches=matches)
