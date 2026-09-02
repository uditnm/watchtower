from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum, DateTime, text

from enum import Enum as PyEnum
from datetime import datetime

class NotificationStatus(PyEnum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class Notification(Base):
    __tablename__ = "notification"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    observation_id: Mapped[int] = mapped_column(ForeignKey("observation.id"), nullable=False)
    status: Mapped[NotificationStatus] = mapped_column(Enum(NotificationStatus), nullable=False)
    attempt_number: Mapped[int] = mapped_column(nullable=False, server_default=text("1"))
    next_attempt_at: Mapped[datetime | None] = mapped_column(DateTime)

    observation: Mapped["Observation"] = relationship("Observation", back_populates="notifications")