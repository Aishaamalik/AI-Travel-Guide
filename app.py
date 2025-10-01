import streamlit as st
from backend import get_travel_recommendations

# Set page configuration
st.set_page_config(
    page_title="AI Travel Guider",
    page_icon="✈️",
    layout="wide"
)

# Title and description
st.title("✈️ AI Travel Guider")
st.markdown("Discover your perfect travel destinations based on your interests!")

# Sidebar for additional features
st.sidebar.header("Travel Preferences")
destination_type = st.sidebar.selectbox(
    "Preferred Destination Type",
    ["Adventure", "Relaxation", "Cultural", "Nature", "City", "Beach", "Mountain", "Any"]
)
budget_range = st.sidebar.selectbox(
    "Budget Range",
    ["Budget", "Mid-range", "Luxury", "Any"]
)
travel_duration = st.sidebar.slider("Travel Duration (days)", 1, 30, 7)

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
                    'travel_style': budget_range.lower() if budget_range != "Any" else "",
                    'trip_length_days': travel_duration,
                    'currency': 'USD',  # Default, can add input later
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
