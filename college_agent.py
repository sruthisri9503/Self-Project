from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load keys
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Select model
model = genai.GenerativeModel("gemini-2.5-flash")

def find_colleges(query: str):
    """
    Returns list of colleges based on user search query.
    """
    
    prompt = f"""
    You are a professional college-finding assistant.
    The user wants to search for colleges. 
    Based on the query below, return the best matching colleges in clear bullet points.

    User Query: {query}

    Format:
    - College Name
    - Location
    - Courses Offered
    - Why it's a good match
    """

    response = model.generate_content(prompt)
    return response.text
