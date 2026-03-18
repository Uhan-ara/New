import streamlit as st
import time
from recommender import recommend_videos

st.set_page_config(page_title="FocusAI", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
</style>
""", unsafe_allow_html=True)



st.sidebar.title("⚙️ Settings")

focus_mode = st.sidebar.checkbox("Enable Focus Mode")

if focus_mode:
    st.warning("🔕 Focus Mode ON: Avoid distractions!")






st.title("📚 FocusAI - Study Video Recommender")
st.info("🚫 No distractions. Only focused learning.")
st.write("Get distraction-free study videos instantly!")

st.warning("⚠️ Some videos may be unavailable. Dataset is manually curated.")

# User input
user_input = st.text_input("Enter topic to study:")

if st.button("Search"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a topic")
    else:
        results = recommend_videos(user_input)

        st.subheader("📚 Recommended Study Videos")

        if len(results) == 0:
            st.error("❌ No relevant study videos found. Try a different topic.")
        else:
            for title, link in results:
                st.markdown(f"### [{title}]({link})")