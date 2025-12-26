
from google import genai
import os

# Use your API Key here
client = genai.Client(api_key="AIzaSyAiBUQu16F1EO8xEZ8sxbaJsegO7xsGqT0") 

def generate_email_summary(email_content):
    try:
        # Switch to the Lite version for higher free limits
        response = client.models.generate_content(
            model="gemini-1.5-flash-8b-exp-0924", 
            contents=f"Summarize this email in two sentences: {email_content}"
        )
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {str(e)}")
        # If even Lite is exhausted, return a helpful message
        return "AI is taking a break (Rate limit reached). Try again in a minute!"