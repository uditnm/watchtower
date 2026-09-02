from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, text, Enum, Text
from datetime import datetime
from enum import Enum as PyEnum

class ExecutionStatus(PyEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class Execution(Base):
    __tablename__ = "execution"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    monitor_id: Mapped[int] = mapped_column(ForeignKey("monitor.id"), nullable=False)
    scheduled_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    status: Mapped[ExecutionStatus] = mapped_column(Enum(ExecutionStatus), nullable=False)
    started_at: Mapped[datetime | None] = mapped_column(DateTime)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime)
    worker_id: Mapped[str | None] = mapped_column(String(255))
    last_heartbeat_at: Mapped[datetime | None] = mapped_column(DateTime)
    attempt_number: Mapped[int] = mapped_column(nullable=False)
    error_message: Mapped[str | None] = mapped_column(Text)
    parent_execution_id: Mapped[int | None] = mapped_column(ForeignKey("execution.id"))

    monitor: Mapped["Monitor"] = relationship("Monitor", back_populates="executions")
    child_executions: Mapped[list["Execution"]] = relationship("Execution", back_populates="parent_execution")
    parent_execution: Mapped["Execution | None"] = relationship("Execution", back_populates="child_executions", remote_side=[id])
    observation: Mapped["Observation | None"] = relationship("Observation", back_populates="execution", cascade="all, delete-orphan")