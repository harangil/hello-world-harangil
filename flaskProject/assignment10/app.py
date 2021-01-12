from flask import Flask
from flask import Flask, redirect, url_for,render_template
from flask import request, session
import mysql.connector



###### App setup
app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
# from pages.about.about import about
# app.register_blueprint(about)

from pages.assignment8.assignment8 import assignment8
app.register_blueprint(assignment8)

from pages.assignment9.assignment9 import assignment9
app.register_blueprint(assignment9)


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

# from pages.delete_user.delete_user import delete_user
# app.register_blueprint(delete_user)

from pages.ex6.ex6 import ex6
app.register_blueprint(ex6)


from pages.footer.footer import footer
app.register_blueprint(footer)

from pages.header.header import header
app.register_blueprint(header)


from pages.insert_user.insert_user import insert_user
app.register_blueprint(insert_user)


from pages.LIST_USERS.LIST_USERS import LIST_USERS
app.register_blueprint(LIST_USERS)

from pages.update_details.update_details import update_details
app.register_blueprint(update_details)




# ## About
# from pages.about.about import about
# app.register_blueprint(about)

## Catalog
# from pages.catalog.catalog import catalog
# app.register_blueprint(catalog)

## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)


###### Components
## Main menu
# from components.main_menu.main_menu import main_menu
# app.register_blueprint(main_menu)
@app.route('/')
def start():
    return render_template('ex6.html')

@app.route('/log_out')
def log_out():
    session['log_in'] = False
    return render_template('ex6.html')


@app.route('/users_list')
def My_Users_List():
    return render_template('LIST_USERS.html')

@app.route('/assignment8')
def My_Hobbies():
    myHobbies = ['Reading','Beer Breawing' ,'Swimming', 'Traveling']
    myBeers = {'Wheat': 'Whinshtefen', 'Stout': ' Guinness', 'Brown Ale': 'Hagibor ', 'Pale Ale': 'Shapira'}
    return render_template('assignment8.html', hobbies = myHobbies,Beers = myBeers)

@app.route('/user_arg')
def user_arg_func():
    if 'user' in request.args:
        currn_user = request.args['user']
        return f'Welcome, {currn_user}'
    return 'in Users'

@app.route('/assignment9' , methods = ['GET','POST'] )
def assignment9_func():
    if request.method == 'GET':
        if 'Name_f' in request.args and 'Name_f' in request.args:
            Name_f = request.args['Name_f']
            Name_l = request.args['Name_l']
            return render_template('assignment9.html', Name_f=Name_f, Name_l=Name_l , method= request.method)
        return render_template('assignment9.html', method= request.method)
    elif request.method == 'POST':

    # if 'Name' in request.args and 'PhoneNum' in request.args:
        name = request.form['Name']
        # name = request.args['Name']
        # phone = request.args['PhoneNum']
        phone = request.form['PhoneNum']
        session['username'] = name
        session['log_in'] = True
        return render_template('assignment9.html' , name = name, phone = phone, method= request.method)
    return render_template('assignment9.html', method=request.method)

    # if 'Name' in request.args and 'PhoneNum' in request.args:
    #     name = request.form['Name']
    #     phone = request.form['PhoneNum']
    #     return render_template('assignment9.html' , name = name, phone = phone)
    #
    # elif 'Name_f' in request.args and 'Name_f' in request.args:
    #     Name_f = request.args['Name_f']
    #     Name_l = request.args['Name_l']
    #     return render_template('assignment9.html', Name_f=Name_f, Name_l=Name_l)

    return render_template('ex6.html' )

def internet_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host = 'localhost',
                                         user = 'root',
                                         passwd = '591235056',
                                         database = 'ex10')
    cursor = connection.cursor(named_tuple = True)
    cursor.execute(query)

    if query_type == 'commit':
        # INSERT UPDATE DELETE
        # returns number of row modified
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # SELECT
        # return query selected or False
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

@app.route('/users')
def users():
    query = "select * from users"
    query_result = internet_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)

@app.route('/insert_user', methods={'GET','POST'})
def insert_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        query = "INSERT INTO users(first_name,last_name,email) VALUES ('%s','%s','%s')" % (first_name,last_name,email)
        internet_db(query=query,query_type='commit')
        return redirect('/users')

    return redirect('/users')

@app.route('/delete_user', methods={'GET','POST'})
def delete_user():
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE id='%s';" % user_id
        internet_db(query=query, query_type='commit')
        return redirect('/users')
    return 'delete user'

@app.route('/update_details', methods={'GET','POST'})
def update_details():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        user_id = request.form['id']
        query = "UPDATE users SET first_name = '%s',last_name='%s',email='%s' WHERE id='%s';" % (first_name,last_name,email,user_id)
        internet_db(query=query, query_type='commit')
        return redirect('/users')
    return 'update user details'



if __name__ == '__main__':
    app.run(debug=True)