from fastapi import FastAPI
from app.api.routes import router
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(title="AI Observability Platform")

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "AI Observability Platform"
    }

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)
