import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load your model without compiling
model = load_model("emotion_model.hdf5", compile=False)

# Your emotion classes (update if needed)
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def predict_emotion(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize to 64x64 as expected by model
    resized = cv2.resize(gray, (64, 64))

    # Normalize and reshape
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 64, 64, 1))  # batch size, height, width, channel

    # Predict
    result = model.predict(reshaped)
    emotion_index = np.argmax(result)
    emotion = emotion_labels[emotion_index]

    return emotion
