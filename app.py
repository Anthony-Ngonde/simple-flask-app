from flask import Flask

app = Flask(__name__)

# app.debug = True

@app.route('/')
def index():
    return "Hello"

@app.route('/about')
def about():
    return "About Page"

@app.route('/hello/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/age/<string:name>/<int:age>')
def show_info(name,age):
    return f"{name} is {age} years old"

if __name__ == "__main__":
    app.run(debug=True)