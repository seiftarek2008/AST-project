import streamlit as st
import os
import random

st.set_page_config(
    page_title="Arabic Sign Quiz Game",
    layout="wide"
)

st.title("🎮 Arabic Sign Language Quiz Game")

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

# ---------------- SESSION ---------------- #

if "score" not in st.session_state:
    st.session_state.score = 0

if "current_image" not in st.session_state:
    st.session_state.current_image = None

if "current_answer" not in st.session_state:
    st.session_state.current_answer = ""

if "options" not in st.session_state:
    st.session_state.options = []

# ---------------- NEW QUESTION ---------------- #

def load_new_question():

    key = random.choice(list(arabic_map.keys()))
    st.session_state.current_answer = arabic_map[key]

    st.session_state.current_image = os.path.join("Alphabet", f"{key}.jpg")

    options = random.sample(letters, 4)

    if st.session_state.current_answer not in options:
        options[random.randint(0, 3)] = st.session_state.current_answer

    st.session_state.options = options


if st.session_state.current_image is None:
    load_new_question()

# ---------------- UI ---------------- #

st.markdown("## 🤟 What letter is this sign?")

if os.path.exists(st.session_state.current_image):
    st.image(st.session_state.current_image, width=300)
else:
    st.error(f"Image not found: {st.session_state.current_image}")

st.markdown(f"### 🏆 Score: {st.session_state.score}")

# ---------------- OPTIONS (FIXED) ---------------- #

choice = st.radio(
    "Choose the correct letter:",
    st.session_state.options
)

# ---------------- CHECK ---------------- #

if st.button("✔ Check Answer"):

    if choice == st.session_state.current_answer:
        st.success("✔ Correct!")
        st.session_state.score += 1
        load_new_question()
        st.rerun()

    else:
        st.error("❌ Wrong answer")

# ---------------- NEXT ---------------- #

if st.button("🎲 Next Question"):
    load_new_question()
    st.rerun()