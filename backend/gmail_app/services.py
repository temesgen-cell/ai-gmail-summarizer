# services.py
import google.generativeai as genai
from django.conf import settings

# Configure Gemini with your API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

def generate_email_summary(email_content):
    """
    Sends email content to Gemini and returns a concise summary.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Summarize the following email content in 2-3 concise sentences. 
        Focus on the main action item or the core message.
        
        Email Content:
        {email_content}
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"AI Summarization Error: {e}")
        return "Could not generate summary at this time."