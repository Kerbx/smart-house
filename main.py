import RPi.GPIO as GPIO
import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/update')
def update():
    return flask.jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)