import streamlit as st
import torch
from PIL import Image
from io import *
import glob
from datetime import datetime
import os
import wget
import cv2
import time
# Configurations
CFG_MODEL_PATH = "yolo\\runs\\train\\exp4\\weights\\best.pt"

def imageInput(model,model1, src):

    if src == 'Upload your own data.':
        image_file = st.file_uploader(
            "Upload An Image", type=['png', 'jpeg', 'jpg'])
        col1, col2,col3 = st.columns(3)
        if image_file is not None:
            img = Image.open(image_file)
            with col1:
                st.image(img, caption='Uploaded Image',
                         use_column_width='always')
            ts = datetime.timestamp(datetime.now())
            imgpath = os.path.join('data/uploads', str(ts)+image_file.name)
            outputpath = os.path.join(
                'data/outputs/5n', os.path.basename(imgpath))
            outputpath1 = os.path.join(
                'data/outputs/5s', os.path.basename(imgpath))
            with open(imgpath, mode="wb") as f:
                f.write(image_file.getbuffer())

            with st.spinner(text="Predicting..."):
                # Load model
                #5n
                t1 = time.time()
                pred = model(imgpath)
                pred.render()
                t2 = time.time()
                y5ntime = t2 - t1
                #5s
                t1 = time.time()
                pred1= model1(imgpath)
                pred1.render()
                t2 = time.time()
                y5stime = t2 - t1
                # save output to file
                for im in pred.ims:
                    im_base64 = Image.fromarray(im)
                    im_base64.save(outputpath)
                for im in pred1.ims:
                    im_base64 = Image.fromarray(im)
                    im_base64.save(outputpath1)

            # Predictions
            img_ = Image.open(outputpath)
            with col2:
                st.image(img_, caption='Yolov5n, {} ms'.format(int(y5ntime*1000)),
                         use_column_width='always')
            img_1 = Image.open(outputpath1)
            with col3:
                st.image(img_1, caption='Yolov5s, {} ms'.format(int(y5stime*1000)),
                         use_column_width='always')


def main():
    if not os.path.exists(CFG_MODEL_PATH):
            st.error(
                'Model not found', icon="⚠️")

    # -- Sidebar
    st.sidebar.title('⚙️ Options')
    datasrc = 'Upload your own data.' 
    option = st.sidebar.radio("Select input type.", ['Image'])
    if torch.cuda.is_available():
        deviceoption = st.sidebar.radio("Select compute Device.", [
                                        'cpu', 0], disabled=False, index=1)
    else:
        deviceoption = st.sidebar.radio("Select compute Device.", [
                                        'cpu', 0], disabled=True, index=0)
    # -- End of Sidebar

    st.header('📦 YOLOv5 cho Nhận Dạng Hàng Hóa Trên Quầy Thanh Toán')

    if option == "Image":
        imageInput(loadmodel(deviceoption),loadv5s(deviceoption), datasrc)


def loadv5s(device):
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path="yolo\\runs\\train\\exp2\\weights\\best.pt", device=device)
    return model        

def loadmodel(device):
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path=CFG_MODEL_PATH, device=device)
    return model


if __name__ == '__main__':
    main()