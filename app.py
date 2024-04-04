from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world, index'

@app.route('/sum')
def sum():
    n1 = 10
    n2 = 20
    result = n1 + n2
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)