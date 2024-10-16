from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, 'site.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.secret_key = "originals255"

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)


    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f"<Employee {self.first_name}"
    

@app.route('/')
def index():
    employees = Employee.query.all()
    context={
        'employees':employees
    }
    return render_template('index.html', **context)


@app.route('/add', methods=["GET","POST"])
def add_employee():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        new_employee = Employee(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_employee)
        db.session.commit()

        flash("Employee added successfully")

        return redirect(url_for('index'))

    
    return render_template('add.html')


@app.route('/update/<int:id>', methods = ['GET','POST'])
def update_employee(id):
    employee_to_be_updated = Employee.query.get_or_404(id)

    if request.method == "POST":
        employee_to_be_updated.first_name = request.form.get('first_name')

        employee_to_be_updated.last_name = request.form.get('last_name')

        employee_to_be_updated.email = request.form.get('email')

        db.session.commit()

        flash("Employee updated successfully")

        return redirect(url_for('index'))

    context={
        'employee':employee_to_be_updated
    }

    return render_template('update.html', **context)


@app.route('/delete/<int:id>')
def delete_employee(id):
    employee_to_delete = Employee.query.get_or_404(id)

    db.session.delete(employee_to_delete) 

    db.session.commit()

    flash("Employee deleted successfully")

    return redirect(url_for('index'))


@app.route('/hello/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/age/<string:name>/<int:age>')
def show_info(name, age):
    return f"{name} is {age} years old"

if __name__ == "__main__":
    with app.app_context():  
        db.create_all()  
    app.run(debug=True)