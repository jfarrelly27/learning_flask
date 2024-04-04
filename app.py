from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum')
def sum():
    n1 = 10
    n2 = 20
    result = n1 + n2
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
