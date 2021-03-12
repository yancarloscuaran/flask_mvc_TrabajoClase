from flask import render_template
from src import app
from src.config.globals as globals

@app.route('/')
def index():
    if(globals.DB == False):
        return render_template('instalacion.html')

    return render_template('index.html')