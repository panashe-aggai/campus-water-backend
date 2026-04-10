from pydantic import BaseModel
from typing import Optional


class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True


class WaterAssetCreate(BaseModel):
    asset_name: str
    asset_type: str
    latitude: float
    longitude: float
    condition_status: str
    photo_path: Optional[str] = None
    notes: Optional[str] = None
    created_by: int


class WaterAssetOut(BaseModel):
    id: int
    asset_name: str
    asset_type: str
    latitude: float
    longitude: float
    condition_status: str
    photo_path: Optional[str] = None
    notes: Optional[str] = None
    created_by: int
    is_verified: bool

    class Config:
        from_attributes = True


class IncidentCreate(BaseModel):
    incident_name: str
    incident_type: str
    related_asset_id: Optional[int] = None
    latitude: float
    longitude: float
    condition_status: str
    severity: Optional[str] = None
    photo_path: Optional[str] = None
    notes: Optional[str] = None
    reported_by: int


class IncidentOut(BaseModel):
    id: int
    incident_name: str
    incident_type: str
    related_asset_id: Optional[int] = None
    latitude: float
    longitude: float
    condition_status: str
    severity: Optional[str] = None
    photo_path: Optional[str] = None
    notes: Optional[str] = None
    reported_by: int
    is_verified: bool

    class Config:
        from_attributes = True