from flask import Blueprint, render_template

# about blueprint definition
LIST_USERS = Blueprint('LIST_USERS', __name__, static_folder='static', static_url_path='/LIST_USERS', template_folder='templates')


# Routes
@LIST_USERS.route('/LIST_USERS')
def index():
    return render_template('LIST_USERS.html')
