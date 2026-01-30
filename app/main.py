from fastapi import FastAPI

# Routers
from app.api.health import router as health_router
from app.api.routes.simulation import router as simulation_router
from app.api.routes.explain import router as explain_router
from app.api.routes.company import router as company_router
from app.api.routes.company_explain import router as company_explain_router
from app.api.routes.company_agent import router as company_agent_router
from app.api.routes.company_compare import router as company_compare_router
from app.api.routes.company_trend import router as company_trend_router
from app.api.routes.company_trend_compare import router as company_trend_compare_router
from app.api.routes.company_upload import router as company_upload_router


app = FastAPI(
    title="Finance Intelligence AI",
    description="AI-powered financial health analysis, simulations, and explanations",
    version="1.0.0"
)

# -------------------------
# API Routers (v1)
# -------------------------

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(simulation_router, prefix="/api/v1", tags=["Simulations"])
app.include_router(explain_router, prefix="/api/v1", tags=["Explanations"])

app.include_router(company_router, prefix="/api/v1")
app.include_router(company_explain_router, prefix="/api/v1")
app.include_router(company_agent_router, prefix="/api/v1")
app.include_router(company_compare_router, prefix="/api/v1")
app.include_router(company_trend_router, prefix="/api/v1")
app.include_router(company_trend_compare_router, prefix="/api/v1")

app.include_router(
    company_upload_router,
    prefix="/api/v1",
    tags=["Company Upload"]
)

# -------------------------
# System Health Check
# -------------------------

@app.get("/health", tags=["System"])
def system_health():
    return {"status": "ok"}