from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
import models
import auth as auth_utils
from routers import auth, patients, rooms, assets, doctors, appointments, admin

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hospital Patient & Asset Tracker",
    description="API for managing hospital patients, rooms, and equipment.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(rooms.router)
app.include_router(assets.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(admin.router)


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "app": "Hospital Tracker API"}


@app.on_event("startup")
def seed_admin():
    db = SessionLocal()
    try:
        existing = auth_utils.get_user_by_email(db, "admin@hospital.com")
        if not existing:
            admin = models.User(
                email="admin@hospital.com",
                full_name="System Admin",
                hashed_password=auth_utils.hash_password("admin123"),
                role=models.UserRole.admin,
                is_verified=True,
            )
            db.add(admin)
            db.commit()
            print("✓ Default admin created — email: admin@hospital.com / password: admin123")
    finally:
        db.close()
