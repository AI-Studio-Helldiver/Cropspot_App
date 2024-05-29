""" Runs prediction from our model.

"""

import cv2
import numpy as np
from tensorflow.keras.models import load_model


class Processor:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def process_image(self, image):
        try:
            # Prepare the frame for the model
            prepared_image = load_image(image)

            # Perform inference
            predictions = self.model.predict(prepared_image)
            class_labels = {0: 'healthy', 1: 'leaf blight', 2: 'leaf curl', 3: 'septoria leaf spot', 4: 'verticulium wilt'}

            # Decode the predictions manually for your custom model
            predicted_class_index = np.argmax(predictions[0])
            predicted_class = class_labels[predicted_class_index]
            confidence = predictions[0][predicted_class_index]

            results = [(predicted_class, confidence)]

            return results
        except Exception as e:
            print(f"Error processing image: {e}")
            return []


def load_image(image_path, target_size=(224, 224)):
    """Loads and preprocesses an image for TensorFlow input.

    Args:
        image_path (str): Path to the image file.
        target_size (tuple, optional): Desired size of the output image (width, height). Defaults to (224, 224).

    Returns:
        np.ndarray: Preprocessed image array ready for TensorFlow input.
    """
    # Load image using OpenCV
    img = cv2.imread(image_path)

    # Check if image loading was successful
    if img is None:
        raise ValueError(f"Could not load image from: {image_path}")

    # Convert BGR to RGB (TensorFlow models expect RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize image to target size
    img = cv2.resize(img, target_size)

    # Convert image to array and add batch dimension
    img_array = np.expand_dims(img, axis=0)

    return img_array
