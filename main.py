import datetime

import streamlit as st
import cv2
import time

st.title('Motion Detector')
start = st.button("Start Camera")

if start:
    st_img = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # current time as datetime object
        dt = datetime.now()

        # Get the date
        cv2.putText(img=frame, text=dt.strftime("%A"), org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,255,255),
                    thickness=2, lineType=cv2.LINE_AA)
        # Get the time
        cv2.putText(img=frame, text=dt.strftime("%H:%M:%S"), org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 64, 64),
                    thickness=2, lineType=cv2.LINE_AA)

        st_img.image(frame)