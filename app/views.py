from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Arialyson'
    cidade = 'Natal-RN'
    context = {
        'usuario': usuario,
        'cidade': cidade
    }
    return render_template('index.html', context=context)

@app.route('/nova/')
def novapag():
    return 'Outra view'