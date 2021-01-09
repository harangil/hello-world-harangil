from flask import Blueprint, render_template

# about blueprint definition
insert_user = Blueprint('insert_user', __name__, static_folder='static', static_url_path='/insert_user', template_folder='templates')


# Routes
@insert_user.route('/insert_user')
def index():
    return render_template('insert_user.html')
