from datetime import datetime
#from core.models import ShortUrls
from core import app
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for
from core.links import reduce

def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        
        short_url = reduce(url)

        return render_template('index.html' , short_url = short_url , user_url = url)

    return render_template('index.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/dmca')
def dmca():
    return render_template('dmca.html')


