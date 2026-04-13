from sqlalchemy.orm import Session
from . import models, schemas


# ================= USERS =================
def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise Exception("User with this email already exists")

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
    db_asset = models.WaterAsset(
        asset_name=asset.asset_name,
        asset_type=asset.asset_type,
        latitude=asset.latitude,
        longitude=asset.longitude,
        condition_status=asset.condition_status,
        photo_path=asset.photo_path,
        notes=asset.notes,
        created_by=asset.created_by,
        is_verified=False
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def get_water_assets(db: Session):
    return db.query(models.WaterAsset).all()


def delete_water_asset(db: Session, asset_id: int):
    asset = db.query(models.WaterAsset).filter(
        models.WaterAsset.id == asset_id
    ).first()

    if not asset:
        return None

    db.delete(asset)
    db.commit()
    return asset


# ================= INCIDENTS =================
def create_incident(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.IncidentReport(
        incident_name=incident.incident_name,
        incident_type=incident.incident_type,
        related_asset_id=incident.related_asset_id,
        latitude=incident.latitude,
        longitude=incident.longitude,
        condition_status=incident.condition_status,
        severity=incident.severity,
        photo_path=incident.photo_path,
        notes=incident.notes,
        reported_by=incident.reported_by,
        is_verified=False
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_incidents(db: Session):
    return db.query(models.IncidentReport).all()


def delete_incident(db: Session, incident_id: int):
    incident = db.query(models.IncidentReport).filter(
        models.IncidentReport.id == incident_id
    ).first()

    if not incident:
        return None

    db.delete(incident)
    db.commit()
    return incident