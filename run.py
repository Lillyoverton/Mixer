from flask import Flask, render_template
app = Flask(__name__)

spirits = [
    'Gin',
    'Rum',
    'Tequila',
    'Vodka',
    'Whiskey',
    'Brandy'
]

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/ingredients')
def ingredients():
    return render_template ('ingredients.html',
                            spirits=spirits)
