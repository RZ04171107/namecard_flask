from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def home(name=None):
    return render_template('index.html', name=name)

# to run the app: $ flask --app server --debug run
