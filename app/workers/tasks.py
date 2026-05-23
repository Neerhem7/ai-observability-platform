import time

from app.workers.celery_worker import celery_app
from app.ml_models.registry import get_model
from app.database import SessionLocal
from app.models.inference_record import InferenceRecord
from app.core.logger import logger
from app.core.metrics import (
REQUEST_COUNTER,
INFERENCE_LATENCY
)


@celery_app.task
def run_inference(model_name, input_data):

    start_time = time.time()

    try:
        logger.info(
            f"Running inference for model: {model_name}"
        )
        model = get_model(model_name)

        prediction = model.predict(input_data)

        latency = time.time() - start_time

        INFERENCE_LATENCY.observe(latency)

        session = SessionLocal()

        record = InferenceRecord(
            model_name=model_name,
            latency=latency,
            status="success"
        )

        session.add(record)
        session.commit()
        session.close()

        logger.info(
            f"Inference latency: {latency:.4f}"
        )

        return {
            "prediction": prediction,
            "latency": latency,
            "status": "success"
        }

    except Exception as e:
        logger.error(str(e))

        record = InferenceRecord(
            model_name=model_name,
            latency=0,
            status="failure"
        )

        session.add(record)
        session.commit()

        return {
            "status": "error",
            "error": str(e)
        }
