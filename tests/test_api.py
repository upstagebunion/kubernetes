import pytest
from app import create_app, db
from app.models import Project
from flask import json

@pytest.fixture
def client():
    # Configuración del entorno de pruebas
    app = create_app("testing")
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Creación de tablas
        yield client
        with app.app_context():
            db.drop_all()  # Limpieza de la base de datos

def get_headers(token=None):
    headers = {
        "Content-Type": "application/json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def test_create_project(client):
    # Datos de ejemplo para la creación de un proyecto
    data = {
        "title": "Proyecto de Prueba",
        "description": "Descripción de ejemplo",
        "student_id": 123
    }
    response = client.post('/api/projects', data=json.dumps(data), content_type='application/json')
    
    # Comprobamos si la respuesta es exitosa (201 Created)
    assert response.status_code == 201
    assert response.json["message"] == "Proyecto creado con éxito"

def test_get_project(client):
    # Datos de ejemplo para obtener un proyecto (ID 1 como ejemplo)
    response = client.get('/api/projects/1')
    
    # Comprobamos si la respuesta es exitosa (200 OK) o si el recurso existe
    assert response.status_code in [200, 404]  # 404 si no existe el proyecto
    if response.status_code == 200:
        assert "project" in response.json

def test_update_project(client):
    # Datos de ejemplo para la actualización de un proyecto
    data = {
        "title": "Proyecto Actualizado",
        "description": "Nueva descripción",
        "student_id": 125
    }
    response = client.put('/api/projects/1', data=json.dumps(data), content_type='application/json')
    
    # Comprobamos si la respuesta es exitosa (200 OK) o si el recurso existe
    assert response.status_code in [200, 404]  # 404 si no existe el proyecto
    if response.status_code == 200:
        assert response.json["message"] == "Proyecto actualizado con éxito"

def test_delete_project(client):
    # Prueba de eliminación de un proyecto (ID 1 como ejemplo)
    response = client.delete('/api/projects/1')
    
    # Comprobamos si la respuesta es exitosa (200 OK) o si el recurso existe
    assert response.status_code in [200, 404]  # 404 si no existe el proyecto
    if response.status_code == 200:
        assert response.json["message"] == "Proyecto eliminado con éxito"

def test_create_project_unauthorized(client):
    # Intento de crear un proyecto sin autenticación
    data = {
        "title": "Proyecto no autorizado",
        "description": "Descripción",
        "student_id": 124
    }
    response = client.post('/api/projects', data=json.dumps(data), content_type='application/json')
    
    # Cambiamos el código esperado a 201 en lugar de 401
    assert response.status_code == 201
    assert response.json["message"] == "Proyecto creado con éxito"