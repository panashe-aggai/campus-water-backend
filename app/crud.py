from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models, schemas


# ================= USERS =================
def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        role=user.role if user.role else "worker",
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ================= WATER ASSETS =================
def create_water_asset(db: Session, asset: schemas.WaterAssetCreate):
    query = text("""
        INSERT INTO water_assets
        (asset_name, asset_type, latitude, longitude, geom, condition_status, photo_path, notes, created_by)
        VALUES
        (:asset_name, :asset_type, :latitude, :longitude,
         ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326),
         :condition_status, :photo_path, :notes, :created_by)
        RETURNING id;
    """)

    result = db.execute(query, {
        "asset_name": asset.asset_name,
        "asset_type": asset.asset_type,
        "latitude": asset.latitude,
        "longitude": asset.longitude,
        "condition_status": asset.condition_status,
        "photo_path": asset.photo_path,
        "notes": asset.notes,
        "created_by": asset.created_by
    })
    db.commit()
    new_id = result.scalar()

    return db.query(models.WaterAsset).filter(models.WaterAsset.id == new_id).first()


def get_water_assets(db: Session):
    return db.query(models.WaterAsset).all()


# ================= INCIDENTS =================
def create_incident(db: Session, incident: schemas.IncidentCreate):
    query = text("""
        INSERT INTO incident_reports
        (incident_name, incident_type, related_asset_id, latitude, longitude, geom,
         condition_status, severity, photo_path, notes, reported_by)
        VALUES
        (:incident_name, :incident_type, :related_asset_id, :latitude, :longitude,
         ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326),
         :condition_status, :severity, :photo_path, :notes, :reported_by)
        RETURNING id;
    """)

    result = db.execute(query, {
        "incident_name": incident.incident_name,
        "incident_type": incident.incident_type,
        "related_asset_id": incident.related_asset_id,
        "latitude": incident.latitude,
        "longitude": incident.longitude,
        "condition_status": incident.condition_status,
        "severity": incident.severity,
        "photo_path": incident.photo_path,
        "notes": incident.notes,
        "reported_by": incident.reported_by
    })
    db.commit()
    new_id = result.scalar()

    return db.query(models.IncidentReport).filter(models.IncidentReport.id == new_id).first()


def get_incidents(db: Session):
    return db.query(models.IncidentReport).all()