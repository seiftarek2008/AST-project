import streamlit as st

st.set_page_config(
    page_title="Arabic Sign Hub",
    page_icon="🤟",
    layout="wide"
)

# ---------------- HIDE SIDEBAR ---------------- #

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: gray;
    margin-bottom: 40px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #ddd;
    text-align: center;
    min-height: 180px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 28px;
    font-weight: bold;
}

.card-text {
    color: gray;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    """
    <div class="main-title">
        🤟 Arabic Sign Hub
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Learn Arabic Sign Language through lessons and interactive games
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- FIRST ROW ---------------- #

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">📚 Learn Signs</div>
        <br>
        <div class="card-text">
            Learn all Arabic sign language letters with images and examples.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Learn Signs", use_container_width=True):
        st.switch_page("pages/1_Arabic Alphabet Sign language.py")

with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">🎮 Quiz Game</div>
        <br>
        <div class="card-text">
            Test your knowledge by identifying sign language letters.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Quiz Game", use_container_width=True):
        st.switch_page("pages/2_Quiz Game.py")

# ---------------- SECOND ROW ---------------- #

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class="card">
        <div class="card-title">🏆 Builder Game</div>
        <br>
        <div class="card-text">
            Build complete Arabic words using sign language.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Builder Game", use_container_width=True):
        st.switch_page("pages/3_Builder Game.py")

with col4:

    st.markdown("""
    <div class="card">
        <div class="card-title">⚡ One Shot Game</div>
        <br>
        <div class="card-text">
            Challenge yourself and answer in a single attempt.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open One Shot Game", use_container_width=True):
        st.switch_page("pages/4_One shot learning game.py")

st.divider()

# ---------------- ABOUT ---------------- #

st.markdown("""
<div class="card">
    <div class="card-title">ℹ️ About Us</div>
    <br>
    <div class="card-text">
        Learn more about the project, its goals, and the team behind it.
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("Open About Us", use_container_width=True):
    st.switch_page("pages/About us.py")

st.divider()

st.info(
    "Recommended path: Learn Signs → Quiz Game → Builder Game → One Shot Game"
)