from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, DateTime, FetchedValue, ForeignKey, Enum, text
from datetime import datetime
from enum import Enum as PyEnum

class MonitorStatus(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Monitor(Base):
    __tablename__ = "monitor"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    config: Mapped[dict] = mapped_column(JSON, nullable=False)
    last_change_detected_at: Mapped[datetime | None] = mapped_column(DateTime)
    next_run_at: Mapped[datetime] = mapped_column(DateTime, nullable = False)
    status: Mapped[MonitorStatus] = mapped_column(Enum(MonitorStatus), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable = False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        nullable = False, 
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), 
        server_onupdate=FetchedValue()
    )

    user: Mapped["User"] = relationship("User", back_populates="monitors")
    executions: Mapped[list["Execution"]] = relationship("Execution", back_populates="monitor", cascade="all, delete-orphan")
    observations: Mapped[list["Observation"]] = relationship("Observation", back_populates="monitor", cascade="all, delete-orphan")