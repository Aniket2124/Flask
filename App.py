from flask import Flask, render_template
from flask.globals import request
from flask.helpers import make_response
from flask.wrappers import Response

app = Flask(__name__)


@app.route('/')
def index():

    #  name = "ANIKET"

    context = {

        'text': 'this is data by index',
        'name': 'Aniket'

    }
    return render_template('index.html', data=context)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/details')
def details():
    return render_template('details.html')


if __name__ == "__main__":
    app.run(debug=True)
