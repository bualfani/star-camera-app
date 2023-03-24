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

        cv2.putText(img=frame, text="Camera Recording", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),
                    thickness=2, lineType=cv2.LINE_AA)