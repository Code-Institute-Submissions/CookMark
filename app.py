import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)