from flask import Blueprint, render_template

# about blueprint definition
assignment9 = Blueprint('assignment9', __name__, static_folder='static', static_url_path='/assignment9', template_folder='templates')


# Routes
@assignment9.route('/assignment9')
def index():
    return render_template('assignment9.html')
