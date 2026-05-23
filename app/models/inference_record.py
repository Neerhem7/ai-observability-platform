from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from app.database import Base


class InferenceRecord(Base):

    __tablename__ = "inference_records"

    id = Column(Integer, primary_key=True)

    model_name = Column(String)

    latency = Column(Float)

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
