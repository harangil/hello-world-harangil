from flask import Blueprint, render_template

# about blueprint definition
delete_user = Blueprint('delete_user', __name__, static_folder='static', static_url_path='/delete_user', template_folder='templates')


# Routes
@delete_user.route('/delete_user')
def index():
    return render_template('delete_user.html')
