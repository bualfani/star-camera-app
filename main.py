import streamlit as st
import cv2

st.title('Motion Detector')
start = st.button("Start Camera")

if start:
    st_img = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = cv2.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
