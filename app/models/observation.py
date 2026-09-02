from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, text, JSON
from datetime import datetime

class Observation(Base):
    __tablename__ = "observation"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    execution_id: Mapped[int] = mapped_column(ForeignKey("execution.id"), nullable=False)
    monitor_id: Mapped[int] = mapped_column(ForeignKey("monitor.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    value: Mapped[dict] = mapped_column(JSON, nullable=False)