from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# ================= USERS =================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="worker", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # 🔥 Relationships (optional but powerful)
    assets = relationship("WaterAsset", back_populates="creator")
    incidents = relationship("IncidentReport", back_populates="reporter")


# ================= WATER ASSETS =================
class WaterAsset(Base):
    __tablename__ = "water_assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    condition_status = Column(String, nullable=False)
    photo_path = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # 🔥 Relationship
    creator = relationship("User", back_populates="assets")


# ================= INCIDENTS =================
class IncidentReport(Base):
    __tablename__ = "incident_reports"

    id = Column(Integer, primary_key=True, index=True)
    incident_name = Column(String, nullable=False)
    incident_type = Column(String, nullable=False)
    related_asset_id = Column(Integer, ForeignKey("water_assets.id"), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    condition_status = Column(String, nullable=False)
    severity = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    reported_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # 🔥 Relationships
    reporter = relationship("User", back_populates="incidents")