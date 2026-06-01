import streamlit as st
from utils.predictor import predict_sign
from PIL import Image
import numpy as np
import cv2
import random

st.set_page_config(
    page_title="Sign Language Word Game",
    layout="wide"
)

st.title("🎮 Sign Language Word Builder Game")

# ---------------- MAP ---------------- #

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
    "zay": "ز",
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

words = ["بيت", "قلم", "مدرسة", "كتاب", "باب"]

# ---------------- SESSION STATE ---------------- #

if "target_word" not in st.session_state:
    st.session_state.target_word = random.choice(words)

if "typed_word" not in st.session_state:
    st.session_state.typed_word = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "last_letter" not in st.session_state:
    st.session_state.last_letter = ""

# ---------------- UI ---------------- #

st.markdown("## 🎯 Target Word")
st.title(st.session_state.target_word)

st.markdown(f"### 🏆 Score: {st.session_state.score}")

# ---------------- CAMERA ---------------- #

img_file = st.camera_input("Show your sign")

if img_file is not None:

    image = Image.open(img_file)
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    label, conf = predict_sign(frame)

    if label is not None and conf >= 0.50:

        label = label.lower().strip()
        letter = arabic_map.get(label, "")

        # منع تكرار نفس الحرف
        if letter and letter != st.session_state.last_letter:
            st.session_state.typed_word += letter
            st.session_state.last_letter = letter

# ---------------- SHOW OUTPUT ---------------- #

st.markdown("## ✍️ Your Word")
st.title(st.session_state.typed_word if st.session_state.typed_word else "—")

# ---------------- CONTROLS ---------------- #

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Delete Last Letter"):
        if st.session_state.typed_word:
            st.session_state.typed_word = st.session_state.typed_word[:-1]

            # تحديث آخر حرف
            st.session_state.last_letter = ""

with col2:
    if st.button("🗑 Clear Word"):
        st.session_state.typed_word = ""
        st.session_state.last_letter = ""

# ---------------- CHECK ---------------- #

if st.button("✔ Check Word"):

    if st.session_state.typed_word == st.session_state.target_word:

        st.success("✔ Correct Word!")

        st.session_state.score += 1
        st.session_state.target_word = random.choice(words)
        st.session_state.typed_word = ""
        st.session_state.last_letter = ""

        st.rerun()

    else:

        st.error("❌ Wrong Word")