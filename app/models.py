from fastai.vision.all import load_learner, PILImage
from io import BytesIO
import torch

class ClassifierModel:
    def __init__(self, model_stream: BytesIO):
        self.model = self.load_model_from_stream(model_stream)

    @staticmethod
    def load_model_from_stream(model_stream: BytesIO):
        model_stream.seek(0)  # Ensure the stream is at the beginning
        return torch.load(model_stream, map_location=torch.device('cpu'))

    def predict(self, image_path: str) -> str:
        image = PILImage.create(image_path)
        prediction = self.model.predict(image)
        return prediction[0]

# Usage example: Initialize from a stream (this should be done in your route)
# model_stream = get_model_from_s3(modelId)
# classifier_model = ClassifierModel(model_stream)
