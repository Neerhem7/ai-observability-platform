from fastapi import APIRouter
from app.workers.tasks import run_inference


router = APIRouter()


@router.post("/predict")
def predict(payload: dict):

    model_name = payload.get('model_name')
    input_data = payload.get('input_data')

    task = run_inference.delay(model_name, input_data)

    return {
        'task_id': task.id,
        'status': 'queued'
    }

@router.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@router.get("/system-status")
def system_status():

    return {
        "api": "running",
        "redis": "connected",
        "worker": "active",
        "database": "healthy"
    }
