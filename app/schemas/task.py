from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from app.models.task import TaskStatus, TaskPriority


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = None


class TaskCreate(TaskBase):
    project_id: int
    
    @validator('due_date')
    def due_date_must_be_future(cls, v):
        if v and v < datetime.now():
            raise ValueError('Due date must be in the future')
        return v


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = None
    
    @validator('due_date')
    def due_date_must_be_future(cls, v):
        if v and v < datetime.now():
            raise ValueError('Due date must be in the future')
        return v


class TaskStatusUpdate(BaseModel):
    status: TaskStatus


class Task(TaskBase):
    id: int
    status: TaskStatus
    project_id: int
    created_by_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    assignee_name: Optional[str] = None
    creator_name: str
    
    class Config:
        from_attributes = True


# Task filters
class TaskFilter(BaseModel):
    status: Optional[TaskStatus] = None
    assignee_id: Optional[int] = None
    priority: Optional[TaskPriority] = None
    overdue_only: bool = False
