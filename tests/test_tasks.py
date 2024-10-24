import pytest
from fastapi.testclient import TestClient
from main import app
from database import create_database, SessionLocal
from models import Task
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    create_database()
    db = SessionLocal()
    yield db
    db.close()

def test_create_task(test_db: Session):
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description", "priority": 1, "due_date": "2023-12-31T23:59:59"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["priority"] == 1
    assert data["due_date"] == "2023-12-31T23:59:59"
    assert data["completed"] == False

def test_read_tasks(test_db: Session):
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_update_task(test_db: Session):
    response = client.post("/tasks/", json={"title": "Task to Update", "description": "Update Description", "priority": 2, "due_date": "2023-12-31T23:59:59"})
    task_id = response.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "description": "Updated Description", "priority": 3, "due_date": "2023-12-31T23:59:59", "completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated Description"
    assert data["priority"] == 3
    assert data["due_date"] == "2023-12-31T23:59:59"
    assert data["completed"] == True

def test_delete_task(test_db: Session):
    response = client.post("/tasks/", json={"title": "Task to Delete", "description": "Delete Description", "priority": 4, "due_date": "2023-12-31T23:59:59"})
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task to Delete"
    assert data["description"] == "Delete Description"
    assert data["priority"] == 4
    assert data["due_date"] == "2023-12-31T23:59:59"
    assert data["completed"] == False
