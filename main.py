import flask
import pin
    
    
app = flask.Flask(__name__)
pin = pin.Pin()


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        if flask.request.form.get('light1') == 'on':
            pin.onPin(5)
        if flask.request.form.get('light1') == 'off':
            pin.offPin(5)
    return flask.render_template('index.html')


@app.route('/update')
def update():
    return flask.jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)