import streamlit as st
from ultralytics import YOLO
@st.cache_resource
def load_model():
    return YOLO(r"C:\Users\Lenovo\PycharmProjects\PythonProject1\model\best.pt")
model = load_model()