from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.models.task import TaskStatus


class TaskStatusCount(BaseModel):
    status: TaskStatus
    count: int


class ProjectTaskReport(BaseModel):
    project_id: int
    project_name: str
    task_counts: List[TaskStatusCount]
    total_tasks: int


class OverdueTask(BaseModel):
    id: int
    title: str
    due_date: datetime
    assignee_name: Optional[str]
    project_name: str
    days_overdue: int
    
    class Config:
        from_attributes = True
