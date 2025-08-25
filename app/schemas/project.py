from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProjectMemberAdd(BaseModel):
    user_id: int


class ProjectMember(BaseModel):
    id: int
    user_id: int
    user_name: str
    user_email: str
    joined_at: datetime

    class Config:
        from_attributes = True


class Project(ProjectBase):
    id: int
    organization_id: int
    created_by_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    members: List[ProjectMember] = []

    class Config:
        from_attributes = True
