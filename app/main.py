from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from app.api.health import router as health_router
from app.api.routes.simulation import router as simulation_router
from app.api.routes.explain import router as explain_router

from app.api.routes.company_upload import router as company_upload_router
from app.api.routes.company_trend import router as company_trend_router
from app.api.routes.company_trend_compare import router as company_trend_compare_router
from app.api.routes.company_explain import router as company_explain_router
from app.api.routes.company_agent import router as company_agent_router

from app.api.routes.individual_upload import router as individual_upload_router

# -------------------------
# Create app FIRST
# -------------------------
app = FastAPI(
    title="Finance Intelligence AI",
    description="AI-powered financial health analysis, simulations, and explanations",
    version="1.0.0"
)

# -------------------------
# CORS
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routers
# -------------------------

# Core
app.include_router(health_router, prefix="/api/v1")
app.include_router(simulation_router, prefix="/api/v1")
app.include_router(explain_router, prefix="/api/v1")

# 👤 Individual
app.include_router(individual_upload_router, prefix="/api/v1")

# 🏢 Company (SINGLE + COMPARE uploads live here)
app.include_router(company_upload_router, prefix="/api/v1")

# Other company features
app.include_router(company_trend_router, prefix="/api/v1")
app.include_router(company_trend_compare_router, prefix="/api/v1")
app.include_router(company_explain_router, prefix="/api/v1")
app.include_router(company_agent_router, prefix="/api/v1")

# -------------------------
# Health
# -------------------------
@app.get("/health")
def system_health():
    return {"status": "ok"}
