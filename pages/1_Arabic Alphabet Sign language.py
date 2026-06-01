import streamlit as st
import os

st.set_page_config(
    page_title="Learn Arabic Sign Language",
    layout="centered"
)

st.title("📚 Learn Arabic Sign Language")

st.write(
    "Choose a letter to see its sign language representation."
)

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

# عكس القاموس: حرف عربي -> اسم الصورة
reverse_map = {v: k for k, v in arabic_map.items()}

selected_letter = st.selectbox(
    "🔤 Choose a letter",
    list(arabic_map.values())
)

image_name = reverse_map[selected_letter]

jpg_path = os.path.join("Alphabet", f"{image_name}.jpg")
png_path = os.path.join("Alphabet", f"{image_name}.png")

st.markdown("---")

st.markdown("## Letter")
st.title(selected_letter)

if os.path.exists(jpg_path):
    st.image(jpg_path, caption=f"Sign for {selected_letter}")
elif os.path.exists(png_path):
    st.image(png_path, caption=f"Sign for {selected_letter}")
else:
    st.error(f"Image not found for {selected_letter}")

st.markdown("---")

st.info(
    "Learn the signs first, then try the Quiz Game and Word Builder Game."
)