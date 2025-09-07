import streamlit as st
import cv2
import numpy as np

st.title("🌱 Simple Soil Moisture Estimator")
st.write("Upload a soil photo to check its moisture status and percentage.")

def estimate_moisture(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    brightness = np.mean(hsv[:, :, 2])
    moisture_percent = max(0, min(100, int(100 - (brightness / 255) * 100)))

    if brightness < 70:
        status = "Wet Soil 💧"
    elif brightness < 130:
        status = "Moist Soil 🌿"
    else:
        status = "Dry Soil 🌵"

    return moisture_percent, status

uploaded_file = st.file_uploader("Upload Soil Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Uploaded Soil Photo", use_container_width=True)

    moisture_percent, status = estimate_moisture(img)

    st.subheader("🌡 Moisture Level")
    st.metric(label="Percentage", value=f"{moisture_percent}%")
    
    st.subheader("📝 Soil Status")
    st.write(f"{status}")

