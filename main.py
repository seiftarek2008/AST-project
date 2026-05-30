import streamlit as st

st.set_page_config(
    page_title="Sign Language Translator",
    page_icon="🤟",
    layout="wide"
)

st.title("🤟AI sign language translator")

st.write(
    """
     capture a sign using your camera.
    The AI model will recognize the sign language gesture.
    """
)