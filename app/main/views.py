from flask import render_template
from . import main

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    title = 'Have fun in under one minute '
    return render_template('index.html', title = title )