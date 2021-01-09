from flask import Blueprint, render_template

# about blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')


# Routes
@header.route('/header')
def index():
    return render_template('header.html')
