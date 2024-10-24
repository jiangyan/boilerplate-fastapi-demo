from fastapi import FastAPI
from routers import tasks, users

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management Application"}

app.include_router(tasks.router)
app.include_router(users.router)
