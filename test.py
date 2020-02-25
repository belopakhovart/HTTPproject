from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/choice/<planet_name>')
def index(planet_name):
    return render_template('index.html', planet_name=planet_name)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')