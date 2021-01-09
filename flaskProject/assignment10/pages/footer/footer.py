from flask import Blueprint, render_template

# about blueprint definition
footer = Blueprint('footer', __name__, static_folder='static', static_url_path='/footer', template_folder='templates')


# Routes
@footer.route('/footer')
def index():
    return render_template('footer.html')
