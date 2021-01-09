from flask import Blueprint, render_template

# about blueprint definition
assignment8 = Blueprint('assignment8', __name__, static_folder='static', static_url_path='/assignment8', template_folder='templates')


# Routes
@assignment8.route('/assignment8')
def index():
    return render_template('assignment8.html')
