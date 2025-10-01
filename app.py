import streamlit as st
import base64
from backend import get_travel_recommendations

# Set page configuration
st.set_page_config(
    page_title="AI Travel Guider",
    page_icon="✈️",
    layout="wide"
)

def set_bg_with_overlay(img_path, overlay_rgba="rgba(255,255,255,0.3)"):
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient({overlay_rgba}, {overlay_rgba}), url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp .css-1d391kg {{ /* container text background tweak (class may vary) */
            background: rgba(255,255,255,0.0);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_sidebar_bg(img_path):
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_with_overlay("pic1.jpg", overlay_rgba="rgba(255,255,255,0.3)")

set_sidebar_bg("pic2a.jpg")

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "About"])

# Custom CSS for travel vibes and text color
st.markdown("""
<style>
    .main {
        color: black;
    }
    .stTitle {
        color: black !important;
        font-weight: bold;
    }
    .stMarkdown {
        color: black !important;
    }
    .recommendations, .recommendations * {
        color: black !important;
    }
    .custom-success {
        color: black !important;
        background-color: rgba(76, 175, 80, 0.2) !important;
        border: 1px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stButton button {
        background-color: white !important;
        color: black !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    .stTextArea textarea {
        background-color: white !important;
        color: black !important;
        border: 1px solid black !important;
    }
    .stTextArea label {
        color: black !important;
    }
    .stSelectbox select, .stSlider {
        background-color: white !important;
        color: black !important;
    }
    .stAlert {
        color: black !important;
    }
    .stSuccess {
        color: black !important;
    }
    .stError {
        color: black !important;
    }
    .stWarning {
        color: black !important;
    }
    .stInfo {
        color: black !important;
    }
    .stSpinner {
        color: black !important;
    }
    .stHeader {
        color: black !important;
    }
    .stTextArea textarea::placeholder {
        color: black !important;
    }
    .css-1v0mbdj.e1fqkh3o3 { /* streamlit title */
        color: black !important;
    }
    .css-1d391kg.e1fqkh3o3 { /* streamlit header */
        color: black !important;
    }
    .css-1d391kg.e1fqkh3o3 { /* streamlit markdown */
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

if page == "Home":
    # Title and description with explicit black color
    st.markdown('<h1 style="color:black;">✈️ AI Travel Guider</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:black;">Discover your perfect travel destinations based on your interests!</p>', unsafe_allow_html=True)

    # Main content
    st.markdown('<h2 style="color:black;">Tell us about your interests</h2>', unsafe_allow_html=True)
    user_interests = st.text_area(
        "What do you love to explore? (e.g., hiking, beaches, historical sites, food, wildlife)",
        height=100,
        placeholder="Describe your travel interests, favorite activities, or types of places you enjoy...",
    )

    # Generate recommendations button
    if st.button("Get Travel Recommendations", type="primary"):
        if user_interests.strip():
            with st.spinner("Generating personalized travel recommendations..."):
                try:
                    # Collect user inputs
                    user_inputs = {
                        'user_interests': user_interests,
                        'currency': 'USD',
                    }
                    recommendations = get_travel_recommendations(user_inputs)

                    # st.success("Here are your personalized travel recommendations!")
                    st.markdown('<div class="custom-success">Here are your personalized travel recommendations!</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="recommendations">{recommendations}</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.info("Please check your Groq API key in the .env file and ensure all dependencies are installed.")
        else:
            st.warning("Please enter your interests to get recommendations.")

elif page == "About":
    st.markdown('<h1 style="color:black;">About AI Travel Guider</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:black;">This app uses AI to provide personalized travel recommendations based on your interests. Powered by Groq AI and built with Streamlit.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:black;">Features:</p>', unsafe_allow_html=True)
    st.markdown('- Personalized destination suggestions\n- Weather information\n- Packing checklists\n- Budget breakdowns\n- Safety tips', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Groq AI")
