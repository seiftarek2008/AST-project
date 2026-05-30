import streamlit as st
from ultralytics import YOLO
import os

@st.cache_resource
def load_model():
    model_path = os.path.join("model", "best.pt")
    return YOLO(model_path)