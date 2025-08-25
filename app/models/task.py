from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum
from app.database import Base


class TaskStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


class TaskPriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        unique=True,
        nullable=False,
    )
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    status = Column(Enum(TaskStatus, name="task_status"), nullable=False, default=TaskStatus.TODO, index=True)
    priority = Column(Enum(TaskPriority, name="task_priority"), nullable=False, default=TaskPriority.MEDIUM)
    due_date = Column(DateTime(timezone=True))
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    project = relationship("Project", back_populates="tasks")
    assignee = relationship(
        "User", foreign_keys=[assignee_id], back_populates="assigned_tasks"
    )
    creator = relationship(
        "User", foreign_keys=[created_by_id], back_populates="created_tasks"
    )
    comments = relationship(
        "Comment", back_populates="task", cascade="all, delete-orphan"
    )
    attachments = relationship(
        "Attachment", back_populates="task", cascade="all, delete-orphan"
    )
