from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

app = Flask(__name__)

employees = {
    1: {"id": 1, "imie": "Jan", "nazwisko": "Kowalski", "stanowisko": "Manager"},
    2: {"id": 2, "imie": "Pan", "nazwisko": "Nowak", "stanowisko": "Developer"},
}

# Endpoint do zwracania wszystkich pracowników
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(list(employees.values()))

# Endpoint do zwracania pracownika o podanym id
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = employees.get(id)
    if employee:
        return jsonify(employee)
    else:
        abort(404)

# Endpoint do dodawania pracownika
@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = request.json
    employee_id = new_employee[0].get("id")
    if employee_id not in employees:
        employees[employee_id] = new_employee[0]
        return "", 202
    else:
        return "", 409

# Endpoint do modyfikowania pracownika o podanym id
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = employees.get(id)
    if employee:
        new_employee_data = request.json
        # Aktualizacja danych pracownika
        for key in new_employee_data:
            employee[key] = new_employee_data[key]
        return "", 202
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
