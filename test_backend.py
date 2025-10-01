from backend import get_travel_recommendations

# Test the backend functionality
if __name__ == "__main__":
    print("Testing AI Travel Guider Backend...")

    # Sample user inputs
    test_inputs = {
        'user_interests': "I love hiking in mountains, exploring ancient ruins, and trying local cuisines.",
        'travel_style': 'adventure',
        'trip_length_days': 7,
        'currency': 'USD'
    }

    try:
        recommendations = get_travel_recommendations(test_inputs)
        print("\nTravel Recommendations:")
        print("=" * 50)
        print(recommendations)
        print("=" * 50)
        print("Backend test successful!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Please check your Groq API key in the .env file.")
