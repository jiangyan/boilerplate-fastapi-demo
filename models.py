from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: int
    due_date: Optional[datetime] = None
    completed: bool

class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str
