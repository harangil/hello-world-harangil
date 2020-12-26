from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('ex6.html')

@app.route('/users_list')
def My_Users_List():
    return render_template('LIST_USERS.html')

@app.route('/assignment8')
def My_Hobbies():
    myHobbies = ['Reading','Beer Breawing' ,'Swimming', 'Traveling']
    myBeers = {'Wheat': 'Whinshtefen', 'Stout': ' Guinness', 'Brown Ale': 'Hagibor ', 'Pale Ale': 'Shapira'}
    return render_template('assignment8.html', hobbies = myHobbies,Beers = myBeers)


if __name__ == '__main__':
    app.run(debug=True)
