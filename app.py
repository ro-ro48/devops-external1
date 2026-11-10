
from flask import Flask, request, jsonify

app = Flask(__name__)

# Two initial students
students = [
    {"id": 101, "name": "Roji"},
    {"id": 102, "name": "Akshaya"}
]

# CREATE - Add student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    student = {
        "id": data["id"],
        "name": data["name"]
    }

    students.append(student)
    return jsonify(student), 201


# READ - Get all students
@app.route('/students', methods=['GET'])
def read_students():
    return jsonify(students), 200


# UPDATE - Update student name
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]
            return jsonify(student), 200

    return jsonify({"message": "Student not found"}), 404


# DELETE - Delete student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"}), 200

    return jsonify({"message": "Student not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
