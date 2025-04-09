import streamlit as st
import cv2
from mood_predictor import predict_emotion
from spotify_helper import get_song_for_mood

st.set_page_config(page_title="Moodify", layout="centered")
st.title("🧠 Moodify - Your Mood-Based Music Recommender")

# Capture image
cap = cv2.VideoCapture(0)
st.text("Capturing image... please allow webcam")

if cap.isOpened():
    ret, frame = cap.read()
    cap.release()

    if ret:
        st.image(frame, caption="Captured Frame", channels="BGR")
        emotion = predict_emotion(frame)
        st.success(f"Detected Mood: {emotion}")

        # Suggest song
        song = get_song_for_mood(emotion)
        if song:
            st.subheader("🎵 Suggested Song Based on Mood:")
            st.markdown(f"[{song['name']} by {song['artist']}]({song['url']})")
        else:
            st.warning("Could not find a suitable song on Spotify.")
    else:
        st.error("Failed to capture image.")
else:
    st.error("Webcam not accessible.")
