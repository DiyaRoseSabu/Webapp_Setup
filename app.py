from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('web_app_home.html')


@app.route('/register')
def reg():
    return render_template('web_app_reg.html')


@app.route('/create')
def create():
    return render_template('web_app_create.html')


@app.route('/write')
def write():
    return render_template('web_app_write.html')


if __name__ == '__main__':
    app.run()