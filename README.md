# Task Management Application

This is a task management application built with FastAPI. It allows users to create, update, and delete tasks. The application also includes user authentication and authorization to ensure that only authorized users can manage tasks. Additional features include task prioritization, due dates, and notifications.

## Setup and Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000` to see the application running.

## API Endpoints

### User Endpoints

- **Register a new user**
  - **URL:** `/users/register`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
    ```

- **Login a user**
  - **URL:** `/users/login`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "access_token": "string",
      "token_type": "string"
    }
    ```

### Task Endpoints

- **Create a new task**
  - **URL:** `/tasks/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "title": "string",
      "description": "string",
      "priority": "integer",
      "due_date": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "priority": "integer",
      "due_date": "string",
      "completed": "boolean"
    }
    ```

- **Get all tasks**
  - **URL:** `/tasks/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": "integer",
        "title": "string",
        "description": "string",
        "priority": "integer",
        "due_date": "string",
        "completed": "boolean"
      }
    ]
    ```

- **Update a task**
  - **URL:** `/tasks/{task_id}`
  - **Method:** `PUT`
  - **Request Body:**
    ```json
    {
      "title": "string",
      "description": "string",
      "priority": "integer",
      "due_date": "string",
      "completed": "boolean"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "priority": "integer",
      "due_date": "string",
      "completed": "boolean"
    }
    ```

- **Delete a task**
  - **URL:** `/tasks/{task_id}`
  - **Method:** `DELETE`
  - **Response:**
    ```json
    {
      "detail": "Task deleted"
    }
    ```
