import streamlit as st
from backend import get_travel_recommendations

# Set page configuration
st.set_page_config(
    page_title="AI Travel Guider",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS for travel vibes
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0E1117 0%, #1a1a2e 50%, #16213e 100%);
        color: #FAFAFA;
    }
    .stTitle {
        color: #00BFFF !important;
        font-weight: bold;
    }
    .stMarkdown {
        color: #FAFAFA;
    }
    .stButton button {
        background-color: #00BFFF !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    .stTextArea textarea {
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border: 1px solid #00BFFF !important;
    }
    .stSelectbox select, .stSlider {
        background-color: #262730 !important;
        color: #FAFAFA !important;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("✈️ AI Travel Guider")
st.markdown("Discover your perfect travel destinations based on your interests!")

# Main content
st.header("Tell us about your interests")
user_interests = st.text_area(
    "What do you love to explore? (e.g., hiking, beaches, historical sites, food, wildlife)",
    height=100,
    placeholder="Describe your travel interests, favorite activities, or types of places you enjoy..."
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

                st.success("Here are your personalized travel recommendations!")
                st.markdown(recommendations)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please check your Groq API key in the .env file and ensure all dependencies are installed.")
    else:
        st.warning("Please enter your interests to get recommendations.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Groq AI")
