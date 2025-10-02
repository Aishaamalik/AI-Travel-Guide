import os
import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Groq API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=2500
)

def get_day_by_day_itinerary(destination, days):
    """
    Generate a detailed day-by-day itinerary for a specific destination.
    """
    prompt = f"""SYSTEM:
You are an expert travel planner. Provide a detailed day-by-day itinerary for the destination "{destination}" over {days} days. Make it engaging, practical, and realistic. Include activities, meals, transportation tips, and any safety notes.

OUTPUT SPEC:
Provide a human-readable markdown format with headings for each day, bullet points for activities, and suggestions for meals/rest.

END.
"""

    response = llm.invoke(prompt)
    return {"human_readable": response.content, "machine_readable": {}}

def get_travel_recommendations(user_inputs):
    """
    Generate travel recommendations based on user inputs.
    Includes destination suggestions, temperature info, survival tips, clothing advice, and more.
    """
    # Extract inputs with defaults
    user_interests = user_inputs.get('user_interests', '')
    home_country = user_inputs.get('home_country', '')
    travel_dates = user_inputs.get('travel_dates', '')
    trip_length_days = user_inputs.get('trip_length_days', '')
    travel_style = user_inputs.get('travel_style', '')
    companions = user_inputs.get('companions', '')
    accessibility_needs = user_inputs.get('accessibility_needs', '')
    currency = user_inputs.get('currency', 'USD')
    climate_pref = user_inputs.get('climate_pref', '')
    max_daily_budget = user_inputs.get('max_daily_budget', '')

    prompt = f"""SYSTEM:
You are an expert travel planner and local guide with up-to-date practical knowledge about destinations, weather, packing, safety, budgeting, and cultural etiquette. Be friendly, concise, and realistic. When making recommendations, prioritize traveler safety and accessibility. Provide both a human-readable, engaging guide and a structured, machine-readable JSON object for app consumption.

USER:
User interests / inputs:
- user_interests: "{user_interests}"               # short comma-separated interests (required)
- home_country: "{home_country}"                   # ISO country or city (optional)
- travel_dates: "{travel_dates}"                   # date range or flexible (optional)
- trip_length_days: {trip_length_days}             # integer (optional)
- travel_style: "{travel_style}"                   # e.g., budget, midrange, luxury, adventure, family
- companions: "{companions}"                       # solo, couple, family, friends
- accessibility_needs: "{accessibility_needs}"     # e.g., wheelchair, limited walking (optional)
- currency: "{currency}"                           # preferred currency, e.g., USD, EUR (optional)
- climate_pref: "{climate_pref}"                   # e.g., warm, cold, mild (optional)
- max_daily_budget: {max_daily_budget}             # numeric (optional)

TASK:
Based on the inputs above, generate a comprehensive travel guide as a human-friendly section (readable text with headings, short paragraphs, and bullet lists) intended for display in Streamlit. Make this engaging, practical, and no more than ~300 words per recommended destination.

REQUIREMENTS & OUTPUT SPEC:
Provide 2-3 destination suggestions that best match the user's interests. For each destination include details like name, country, why it matches, current weather, best time to visit, budget, activities, attractions, packing, safety, accessibility, itinerary, cultural tips, and contact info.

Include a packing checklist categorized into Documents, Clothing, Health & First Aid, Electronics, Food & Water, Weather-specific, Safety & Navigation, Misc.

Provide a quick summary, itinerary hints, and budget breakdown.

Weather: Include temperatures in Celsius and Fahrenheit, with source and timestamp.


8. Safety & legal:
   - Do NOT give medical, legal, or professional emergency advice beyond general first-aid basics. For medical issues, instruct users to contact local emergency services.
   - If an activity might be risky (e.g., glacier hiking, deep water diving), flag it clearly and recommend certified guides.

9. Tone & style:
   - Friendly, actionable, and local-savvy. Use short paragraphs, headings, bullet lists, and bold important warnings.
   - Avoid jargon. Use plain language.

10. Extra features (optional if relevant):
   - Suggested packing checklist download filename suggestion (e.g., "PackingChecklist_TopDestination.pdf")
   - Local phrases (2-3 useful phrases) and pronunciations
   - Transport tips (how to get around, typical taxi fare estimate)
   - Sustainability tips (how to travel responsibly)

EXAMPLE (input -> desired JSON snippet):
Input: user_interests = "mountain hiking, waterfalls, local food"; travel_style="adventure", trip_length_days=7, currency="USD"
Output: Provide `human_readable` markdown and `machine_readable` JSON with keys such as RecommendedDestinations, PackingChecklist, QuickSummary, ItineraryBuilderHints, BudgetBreakdown.

END.
"""

    response = llm.invoke(prompt)
    # Try to parse the response content as JSON to get structured data
    try:
        data = json.loads(response.content)
        return data
    except json.JSONDecodeError:
        # If parsing fails, fallback to returning raw content as human_readable text
        return {"human_readable": response.content, "machine_readable": {}}
