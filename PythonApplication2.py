# -*- coding: cp1251 -*-

import pickle
from flask import *

app = Flask(__name__)





@app.route('/user/<int:id>')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@app.route('/')
def http_404_handler():
    return make_response("404 Error", 400)

@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60*60*24*15)
    res.set_cookie("favorite-font", "sans-serif", 60*60*24*15)
    return res

@app.route('/transfer')
def transfer():
    return redirect("https://localhost:5000/login", code=301)


@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_request(response):
    print("after_request() called")
    return response


@app.route('/books/')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res



if __name__ == "__main__":
    app.run(debug=True)






