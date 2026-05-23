from app.ml_models.sentiment_model import SentimentModel


MODEL_REGISTRY = {
    "sentiment": SentimentModel()
}


def get_model(model_name: str):

    model = MODEL_REGISTRY.get(model_name)

    if not model:
        raise ValueError(
            f"Model {model_name} not found"
        )

    return model
