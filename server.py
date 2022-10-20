from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(name=None):
    return render_template('index.html', name=name)


# to run the app: $ flask --app server --debug run
