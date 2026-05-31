import streamlit as st
from utils.predictor import predict_sign
from PIL import Image
import numpy as np
import cv2
import random
import os

st.set_page_config(
    page_title="Arabic Sign Language Game",
    layout="wide"
)

st.title("🎮 Arabic Sign Language Learning Game")

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

letters = list(arabic_map.values())
reverse_map = {v: k for k, v in arabic_map.items()}

# ---------------- SESSION STATE ---------------- #

if "target_letter" not in st.session_state:
    letter = random.choice(letters)
    st.session_state.target_letter = letter
    st.session_state.locked_target = letter

if "locked_target" not in st.session_state:
    st.session_state.locked_target = st.session_state.target_letter

if "score" not in st.session_state:
    st.session_state.score = 0

if "detected_letter" not in st.session_state:
    st.session_state.detected_letter = ""

if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

# ---------------- TARGET ---------------- #

st.markdown("## 🎯 Target Letter")
st.title(st.session_state.locked_target)

st.markdown(f"### 🏆 Score: {st.session_state.score}")

# ---------------- NEW LETTER ---------------- #

if st.button("🎲 New Letter"):

    new_letter = random.choice(letters)

    st.session_state.target_letter = new_letter
    st.session_state.locked_target = new_letter
    st.session_state.detected_letter = ""
    st.session_state.show_hint = False

    st.rerun()

# ---------------- CAMERA ---------------- #

img_file = st.camera_input("Show the sign")

if img_file is not None:

    image = Image.open(img_file)
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    label, conf = predict_sign(frame)

    if label is not None and conf >= 0.50:

        label = label.lower().strip()

        if label in arabic_map:
            st.session_state.detected_letter = arabic_map[label]

# ---------------- DETECTED ---------------- #

st.markdown("### 🤚 Detected Letter")

if st.session_state.detected_letter:
    st.title(st.session_state.detected_letter)
else:
    st.title("—")

# ---------------- CHECK ---------------- #

if st.button("✔ Check Answer"):

    detected = st.session_state.detected_letter
    target = st.session_state.locked_target

    if not detected:

        st.warning("No sign detected")

    elif detected == target:

        st.success("✔ Correct!")

        st.session_state.score += 1

        new_letter = random.choice(letters)

        st.session_state.target_letter = new_letter
        st.session_state.locked_target = new_letter
        st.session_state.detected_letter = ""
        st.session_state.show_hint = False

        st.rerun()

    else:

        st.session_state.show_hint = True

# ---------------- HINT ---------------- #

if st.session_state.show_hint:

    st.error(
        f"❌ Wrong sign\n\n"
        f"Target: {st.session_state.locked_target}\n"
        f"Detected: {st.session_state.detected_letter}"
    )

    key_name = reverse_map.get(st.session_state.locked_target)

    if key_name:

        jpg_path = f"Alphabet/{key_name}.jpg"
        png_path = f"Alphabet/{key_name}.png"

        if os.path.exists(jpg_path):

            st.markdown("### 📌 Correct Sign")
            st.image(jpg_path)

        elif os.path.exists(png_path):

            st.markdown("### 📌 Correct Sign")
            st.image(png_path)

        else:

            st.warning(
                f"No image found for {key_name}\n"
                f"Expected: {jpg_path} or {png_path}"
            )