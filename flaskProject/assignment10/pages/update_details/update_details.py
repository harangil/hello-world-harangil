from flask import Blueprint, render_template

# about blueprint definition
update_details = Blueprint('update_details', __name__, static_folder='static', static_url_path='/update_details', template_folder='templates')


# Routes
@update_details.route('/update_details')
def index():
    return render_template('update_details.html')
