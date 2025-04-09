import streamlit as st
import cv2
from mood_predictor import predict_emotion

st.title("Moodify - Real-time Mood Detection")

frame_placeholder = st.empty()

# Capture video from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Webcam not found.")
else:
    st.success("Webcam connected!")

while True:
    ret, frame = cap.read()
    if not ret:
        st.warning("Failed to capture frame")
        break

    # Predict emotion
    emotion = predict_emotion(frame)

    # Overlay emotion on frame
    cv2.putText(frame, f'Emotion: {emotion}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2, cv2.LINE_AA)

    # Convert color and display
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")

cap.release()
