from flask import Flask, render_template, url_for

app = Flask(__name__)

# app.debug = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hello/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/age/<string:name>/<int:age>')
def show_info(name,age):
    return f"{name} is {age} years old"


if __name__ == "__main__":
    app.run(debug=True)