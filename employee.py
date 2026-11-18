
import re

def validate_employee(data):
    if not data:
        return "Employee details are required"

    required_fields = [
        "employee_id",
        "name",
        "email",
        "department",
        "salary"
    ]

    for field in required_fields:
        if field not in data or data[field] in (None, ""):
            return f"{field} is required"

    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
                    data["email"]):
        return "Invalid email address"

    try:
        if float(data["salary"]) <= 0:
            return "Salary must be greater than zero"
    except (ValueError, TypeError):
        return "Salary must be a valid number"

    return None
