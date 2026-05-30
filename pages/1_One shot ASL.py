import streamlit as st
from utils.predictor import predict_sign
from PIL import Image
import numpy as np
import cv2
st.set_page_config(
    page_title="Arabic Sign Language Detection",
    layout="wide"
)
st.title("🤟 Arabic Sign Language Detection")

arabic_map = {
    "aleff": "ا",
    "al": "ال",
    "bb": "ب",
    "ta": "ت",
    "thaa": "ث",
    "jeem": "ج",
    "haa": "ح",
    "khaa": "خ",
    "dal": "د",
    "thal": "ذ",
    "ra": "ر",
    "dha": "ظ",
    "seen": "س",
    "sheen": "ش",
    "saad": "ص",
    "dhad": "ض",
    "taa": "ط",
    "ain": "ع",
    "ghain": "غ",
    "fa": "ف",
    "gaaf": "ق",
    "kaaf": "ك",
    "laam": "ل",
    "meem": "م",
    "nun": "ن",
    "ha": "ه",
    "waw": "و",
    "yaa": "ي",
    "la": "لا",
    "toot": "ة"
}

if "word" not in st.session_state:
    st.session_state.word = ""

if "last_letter" not in st.session_state:
    st.session_state.last_letter = ""

if "stable_count" not in st.session_state:
    st.session_state.stable_count = 0

if "current_letter" not in st.session_state:
    st.session_state.current_letter = ""

img_file = st.camera_input("Take a sign photo")

if img_file is not None:

    image = Image.open(img_file)
    frame = np.array(image)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    label, conf = predict_sign(frame)

    st.write("Label =", label)
    st.write("Confidence =", conf)

    if label is not None and conf >= 0.50:

        label = label.lower().strip()
        letter = arabic_map.get(label, "")

        st.session_state.current_letter = letter

        if letter == st.session_state.last_letter:
            st.session_state.stable_count += 1
        else:
            st.session_state.stable_count = 0
            st.session_state.last_letter = letter

        if st.session_state.stable_count >= 3 and letter != "":
            st.session_state.word += letter
            st.session_state.stable_count = 0

    else:
        st.session_state.stable_count = 0

st.markdown("### Current Letter")
st.write(st.session_state.current_letter)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add Letter"):
        if st.session_state.current_letter:
            st.session_state.word += st.session_state.current_letter
            st.session_state.stable_count = 0

with col2:
    if st.button("Space"):
        st.session_state.word += " "

with col3:
    if st.button("Delete"):
        st.session_state.word = st.session_state.word[:-1]

with col4:
    if st.button("Clear"):
        st.session_state.word = ""

st.markdown("### Text")
st.text_area("", value=st.session_state.word, height=150, disabled=True)