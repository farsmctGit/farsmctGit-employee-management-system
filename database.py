
import sqlite3

def get_connection():
    return sqlite3.connect("employees.db")

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT,
            salary REAL CHECK (salary > 0)
        )
    """)
    conn.commit()
    conn.close()

def add_employee(data):
    conn = get_connection()
    conn.execute("""
        INSERT INTO employees
        (employee_id, name, email, department, salary)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["employee_id"],
        data["name"],
        data["email"],
        data["department"],
        data["salary"]
    ))
    conn.commit()
    conn.close()

def get_employees():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM employees")
    employees = [
        dict(zip(
            ["employee_id", "name", "email",
             "department", "salary"], row
        ))
        for row in cursor.fetchall()
    ]
    conn.close()
    return employees
