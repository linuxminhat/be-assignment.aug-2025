from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    task_id: int


class CommentUpdate(BaseModel):
    content: str


class Comment(CommentBase):
    id: int
    task_id: int
    user_id: int
    user_name: str
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True


class AttachmentUpload(BaseModel):
    task_id: int


class Attachment(BaseModel):
    id: int
    filename: str
    original_filename: str
    file_size: int
    content_type: Optional[str]
    task_id: int
    uploaded_by_id: int
    uploader_name: str
    uploaded_at: datetime
    
    class Config:
        from_attributes = True
