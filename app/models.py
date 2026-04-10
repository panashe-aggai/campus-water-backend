from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey, Float
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())


class WaterAsset(Base):
    __tablename__ = "water_assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_name = Column(String(150), nullable=False)
    asset_type = Column(String(50), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    condition_status = Column(String(30), nullable=False)
    photo_path = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


class IncidentReport(Base):
    __tablename__ = "incident_reports"

    id = Column(Integer, primary_key=True, index=True)
    incident_name = Column(String(150), nullable=False)
    incident_type = Column(String(50), nullable=False)
    related_asset_id = Column(Integer, ForeignKey("water_assets.id"), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    condition_status = Column(String(30), nullable=False)
    severity = Column(String(20), nullable=True)
    photo_path = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    reported_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())