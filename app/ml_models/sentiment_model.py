from transformers import pipeline


class SentimentModel:

    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis"
        )

    def predict(self, text:str):
        result = self.classifier(text)
        return result
