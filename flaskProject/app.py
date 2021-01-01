from flask import Flask, redirect, url_for,render_template
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'


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



if __name__ == '__main__':
    app.run(debug=True)
