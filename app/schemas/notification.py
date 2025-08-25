from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.models.notification import NotificationType


class NotificationBase(BaseModel):
    type: NotificationType
    title: str
    message: str


class NotificationCreate(NotificationBase):
    user_id: int
    task_id: Optional[int] = None


class Notification(NotificationBase):
    id: int
    is_read: bool
    user_id: int
    task_id: Optional[int]
    created_at: datetime
    
    class Config:
        from_attributes = True


class NotificationMarkRead(BaseModel):
    notification_ids: List[int]
