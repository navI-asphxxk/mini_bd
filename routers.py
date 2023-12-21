from config import app
from flask import request, render_template, jsonify
import services
from data import add_data
from models import Contact
from services import ServiceDB


#add_data()
# db = ServiceDB('company.db')
# db.create_tables()
# db.fill_tables()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/customers', methods=['POST'])
def post_customers():
    if request.is_json:
        return services.create_customers(request.get_json())
    return {}


@app.route('/customers', methods=['GET'])
def get_customers():
    data = services.get_customers()
    return render_template("customers.html", json_data=data.get_json())


@app.route('/customers/<pk>', methods=['GET'])
def get_customer_detail(pk: int):
    data = services.get_customer_detail(pk)
    return render_template("customers.html", json_data=data.get_json())


@app.route('/executors', methods=['POST'])
def post_executors():
    if request.is_json:
        return services.create_executors(request.get_json())
    return {}


@app.route('/executors', methods=['GET'])
def get_executors():
    data = services.get_executors()
    return render_template("executors.html", json_data=data.get_json())


@app.route('/executors/<pk>', methods=['GET'])
def get_executor_detail(pk: int):
    data = services.get_executor_detail(pk)
    return render_template("executors.html", json_data=data.get_json())


@app.route('/issues', methods=['POST'])
def post_issues():
    if request.is_json:
        return services.create_issues(request.get_json())
    return {}


@app.route('/issues', methods=['GET'])
def get_issues():
    data = services.get_issues()
    return render_template('issues.html', json_data=data.get_json())


@app.route('/issues/<pk>', methods=['GET'])
def get_issue_detail(pk: int):
    data = services.get_issue_detail(pk)
    return render_template('issues.html', json_data=data.get_json())


@app.route('/contacts', methods=['POST'])
def post_contacts():
    if request.is_json:
        return services.create_contacts(request.get_json())
    return {}


@app.route('/contacts', methods=['GET'])
def get_contacts():
    data = services.get_contacts()
    return render_template('contacts.html', json_data=data.get_json())


@app.route('/contacts/<pk>', methods=['GET'])
def get_contact_detail(pk: int):
    data = services.get_contact_detail(pk)
    return render_template('contacts.html', json_data=data.get_json())
