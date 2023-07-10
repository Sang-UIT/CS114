import streamlit as st
import torch
from PIL import Image
from io import *
import glob
from datetime import datetime
import os
import wget
from video_predict import runVideo
import cv2

def imageInput(model, src):
    pred = model(src)
    pred.render()
            # save output to file
    return st.image(pred)
    
def loadmodel(device):
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path="yolov5\\runs\\train\\exp4\\weights\\best.pt", device=device)
    return model

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
model=loadmodel(0)
while run:
    _, frame = camera.read()
    
    FRAME_WINDOW.image(imageInput(model, frame))
    
else:
    st.write('Stopped')
    
