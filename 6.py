# -*- coding: cp1251 -*-


from flask import *


app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)



if __name__ == "__main__":
    app.run(debug=True)






