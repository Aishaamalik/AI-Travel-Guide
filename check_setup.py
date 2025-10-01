import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if API key is set
api_key = os.getenv("GROQ_API_KEY")
if api_key and api_key != "YOUR_API_KEY_HERE":
    print("✅ Groq API key is set correctly.")
    print(f"API Key: {api_key[:10]}...")  # Show first 10 characters for verification
else:
    print("❌ Groq API key is not set or is still the placeholder.")
    print("Please update the .env file with your actual Groq API key.")

# Check if required packages can be imported
try:
    import streamlit
    print("✅ Streamlit is installed.")
except ImportError:
    print("❌ Streamlit is not installed.")

try:
    from langchain_groq import ChatGroq
    print("✅ LangChain Groq is installed.")
except ImportError:
    print("❌ LangChain Groq is not installed.")

try:
    import dotenv
    print("✅ Python-dotenv is installed.")
except ImportError:
    print("❌ Python-dotenv is not installed.")

print("\nSetup check complete!")
