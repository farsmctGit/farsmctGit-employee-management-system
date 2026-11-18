
from flask import Flask, request, jsonify
from database import init_db, add_employee, get_employees
from employee import validate_employee

app = Flask(__name__)

# Initialize database
init_db()

@app.route("/")
def home():
    return "Employee Management System"

# Get all employees
@app.route("/employees", methods=["GET"])
def employees():
    return jsonify(get_employees())

# Add a new employee
@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    error = validate_employee(data)
    if error:
        return jsonify({"error": error}), 400

    try:
        add_employee(data)
        return jsonify({
            "message": "Employee added successfully"
        }), 201
    except Exception:
        return jsonify({
            "error": "Unable to add employee"
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
