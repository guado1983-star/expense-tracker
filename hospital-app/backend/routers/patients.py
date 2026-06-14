from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from auth import get_current_user
from controllers import patient_controller

router = APIRouter(prefix="/patients", tags=["patients"])


def _require_not_patient(current_user: models.User):
    if current_user.role == models.UserRole.patient:
        raise HTTPException(status_code=403, detail="Patients cannot perform this action")


def _require_write_access(current_user: models.User):
    if current_user.role == models.UserRole.patient:
        raise HTTPException(status_code=403, detail="Read-only access")


def _get_assigned_patient_user_ids(db, doctor_id: int):
    return {
        row[0]
        for row in db.query(models.Appointment.patient_id)
        .filter(models.Appointment.doctor_id == doctor_id)
        .all()
    }


@router.get("/me", response_model=schemas.PatientOut)
def get_my_chart(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != models.UserRole.patient:
        raise HTTPException(status_code=403, detail="Only patients can access this endpoint")
    patient = db.query(models.Patient).filter(models.Patient.user_id == current_user.id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="No chart found for this account")
    return patient


@router.get("/", response_model=schemas.PaginatedPatients)
def list_patients(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    search: str = Query(''),
    status: str = Query(''),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    _require_not_patient(current_user)
    if current_user.role == models.UserRole.doctor:
        assigned_user_ids = _get_assigned_patient_user_ids(db, current_user.id)
        items = db.query(models.Patient).filter(
            models.Patient.user_id.in_(assigned_user_ids)
        ).all()
        return {"total": len(items), "page": 1, "pages": 1, "items": items}
    return patient_controller.get_all(db, page, limit, search, status)


@router.post("/", response_model=schemas.PatientOut, status_code=status.HTTP_201_CREATED)
def create_patient(
    data: schemas.PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    _require_write_access(current_user)
    return patient_controller.create(db, data)


@router.get("/{patient_id}", response_model=schemas.PatientOut)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    _require_not_patient(current_user)
    patient = patient_controller.get_by_id(db, patient_id)
    if current_user.role == models.UserRole.doctor:
        assigned = _get_assigned_patient_user_ids(db, current_user.id)
        if patient.user_id not in assigned:
            raise HTTPException(status_code=403, detail="Not your patient")
    return patient


@router.put("/{patient_id}", response_model=schemas.PatientOut)
def update_patient(
    patient_id: int,
    data: schemas.PatientUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    _require_write_access(current_user)
    if current_user.role == models.UserRole.doctor:
        patient = patient_controller.get_by_id(db, patient_id)
        assigned = _get_assigned_patient_user_ids(db, current_user.id)
        if patient.user_id not in assigned:
            raise HTTPException(status_code=403, detail="Not your patient")
    return patient_controller.update(db, patient_id, data)


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    _require_write_access(current_user)
    patient_controller.delete(db, patient_id)
