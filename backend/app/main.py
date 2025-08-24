from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .db.session import init_db
from .api.routes.health import router as health_router
from .api.routes.me import router as me_router
from .api.routes.medicines import router as medicines_router
from .api.routes.devices import router as devices_router

app = FastAPI(title="Swaasth Elder Health API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup() -> None:
    init_db()

app.include_router(health_router, prefix="/api")
app.include_router(me_router, prefix="/api")
app.include_router(medicines_router, prefix="/api/medicines", tags=["medicines"]) 
app.include_router(devices_router, prefix="/api/devices", tags=["devices"])