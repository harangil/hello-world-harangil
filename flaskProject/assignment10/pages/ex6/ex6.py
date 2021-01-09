from flask import Blueprint, render_template

# about blueprint definition
ex6 = Blueprint('ex6', __name__, static_folder='static', static_url_path='/ex6', template_folder='templates')


# Routes
@ex6.route('/ex6')
def index():
    return render_template('ex6.html')
