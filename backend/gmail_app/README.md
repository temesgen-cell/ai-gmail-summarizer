 AI Email Summarizer
A full-stack web application that connects to your Gmail, fetches your latest messages, and uses Google Gemini AI to generate concise, two-sentence summaries. Built with a focus on productivity and clean AI integration.

 Features
Gmail OAuth2 Integration: Securely login using your Google account.

Real-time Fetching: Pulls the most recent emails directly from the Gmail API.

AI Summarization: Utilizes gemini-1.5-flash-lite to distill long emails into actionable insights.

Clean UI: Modern React frontend with a responsive design for quick scanning.

 Tech Stack
Frontend: React (Vite), Axios, CSS3

Backend: Django, Django REST Framework

AI Engine: Google Gemini API (google-genai SDK)

Authentication: Google OAuth 2.0

 Setup & Installation
1. Prerequisites
Python 3.10+

Node.js 18+

A Google Cloud Project with Gmail API and Generative Language API enabled.

2. Backend Setup
Bash

cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
3. Frontend Setup
Bash

cd frontend
npm install
npm run dev
4. Environment Variables
Create a .env file in the backend/ folder:

Code snippet

GEMINI_API_KEY=your_google_gemini_key
GOOGLE_CLIENT_ID=your_oauth_id
GOOGLE_CLIENT_SECRET=your_oauth_secret
 Troubleshooting Quota Issues
If you encounter a 429 RESOURCE_EXHAUSTED error:

Ensure you are using the gemini-1.5-flash-lite model in services.py.

Confirm that a Billing Account is linked to your Google Cloud Project (even for the free tier).

Check the Google AI Studio to verify your API key is activ