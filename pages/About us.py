import streamlit as st

st.set_page_config(
    page_title="About Us",
    layout="wide"
)

st.title("👥 Who Are We?")

st.header("Our Team")
st.write(
    """
    We are a group of high school students who are passionate about technology
    and using it to create solutions that positively impact our community.
    Through software development and artificial intelligence, we aim to build
    projects that address real-world challenges and make a meaningful difference.
    """
)

st.header("Our Goal")

st.write(
    """
    We noticed that learning sign language can be difficult for many people,
    creating communication barriers between deaf individuals and the wider community.
    To help address this challenge, we developed Arabic Sign Hub, an interactive
    platform that combines education, artificial intelligence, and gamified learning
    experiences to make sign language more accessible and enjoyable to learn.
    """
)

st.header("Our Vision")

st.write(
    """
    We believe that communication should be accessible to everyone.
    Our vision is to help bridge the gap between deaf individuals and the rest
    of society by providing engaging and effective learning tools that encourage
    more people to learn sign language.
    """
)

st.header("Future Plans")

st.write(
    """
    This project is only the beginning. We are committed to continuously improving
    Arabic Sign Hub by adding more educational content, developing new interactive
    games, enhancing the accuracy of our artificial intelligence models, and
    supporting additional sign languages in the future.

    Our long-term goal is to create a platform that can benefit learners worldwide
    and contribute to a more inclusive society where communication barriers are reduced.
    """
)

st.header("Our Commitment")

st.write(
    """
    We do not see this project as a one-time achievement. We are dedicated to
    expanding and refining it so that it can reach more people and create a
    lasting positive impact. We will continue learning, improving, and innovating
    to ensure that Arabic Sign Hub remains a valuable resource for sign language learners.
    """
)

st.success(
    "🤟 Together, we can make communication more accessible for everyone."
)