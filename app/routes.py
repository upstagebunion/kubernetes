from flask import Blueprint, request, jsonify
from app.models import db, Student, Project
from app.schemas import StudentSchema, ProjectSchema

api = Blueprint('api', __name__)
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

@api.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created"}), 201

@api.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(title=data['title'], description=data['description'], student_id=data['student_id'])
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Proyecto creado con éxito"}), 201

@api.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    students_data = students_schema.dump(students)
    return jsonify(students_data), 200

# Ruta para obtener un estudiante por id
@api.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return {"error": "Estudiante no encontrado"}, 404
    student_data = student_schema.dump(student)
    return jsonify(student_data), 200

@api.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    projects_data = projects_schema.dump(projects)
    return jsonify(projects_data), 200

# Ruta para obtener un estudiante por id
@api.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return {"error": "Proyecto no encontrado"}, 404
    project_data = project_schema.dump(project)
    return jsonify(project_data), 200

@api.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    # Buscamos el estudiante por su ID
    student = Student.query.get(student_id)
    
    if not student:
        return {"error": "Estudiante no encontrado"}, 404
    
    # Obtenemos los datos de la solicitud (en formato JSON)
    data = request.get_json()

    # Actualizamos los campos del estudiante
    student.name = data.get('name', student.name)
    student.email = data.get('email', student.email)
    
    # Guardamos los cambios en la base de datos
    db.session.commit()
    
    # Serializamos el estudiante actualizado y lo devolvemos
    student_data = student_schema.dump(student)
    return jsonify(student_data), 200

@api.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    # Buscamos el estudiante por su ID
    student = Student.query.get(student_id)
    
    if not student:
        return {"error": "Estudiante no encontrado"}, 404
    
    # Eliminamos al estudiante
    db.session.delete(student)
    db.session.commit()
    
    # Respondemos con un mensaje de éxito
    return jsonify({"message": "Estudiante eliminado exitosamente"}), 200

@api.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    # Buscamos el proyecto por su ID
    project = Project.query.get(project_id)
    
    if not project:
        return {"error": "Proyecto no encontrado"}, 404
    
    # Obtenemos los datos de la solicitud (en formato JSON)
    data = request.get_json()

    # Actualizamos los campos del proyecto
    project.title = data.get('title', project.title)
    project.description = data.get('description', project.description)
    project.student_id = data.get('student_id', project.student_id)
    
    # Guardamos los cambios en la base de datos
    db.session.commit()
    
    # Serializamos el proyecto actualizado y lo devolvemos
    project_data = project_schema.dump(project)
    return jsonify(project_data), 200

@api.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    # Buscamos el proyecto por su ID
    project = Student.query.get(project_id)
    
    if not project:
        return {"error": "Proyecto no encontrado"}, 404
    
    # Eliminamos al proyecto
    db.session.delete(project)
    db.session.commit()
    
    # Respondemos con un mensaje de éxito
    return jsonify({"message": "Proyecto eliminado exitosamente"}), 200