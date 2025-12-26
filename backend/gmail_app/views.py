from django.shortcuts import render, redirect
import os
import json
from django.urls import reverse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
#here the new imports

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmailMessage
from .services import generate_email_summary


# Google OAuth2 client ID and secret
CLIENT_SECRETS_FILE = os.path.join(settings.BASE_DIR, 'credentials.json')
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

REDIRECT_URI = 'http://localhost:8000/google/callback/'


def home(request):
    return HttpResponse("Welcome! <a href='/google/login/'>Login with Google</a>")

def google_login(request):
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    flow.redirect_uri = 'http://localhost:8000/google/callback/'

    authorization_url, state = flow.authorization_url(access_type='offline', prompt='consent')

    # Store the state in the session for later use
    request.session['state'] = state

    return redirect(authorization_url)

@api_view(['GET'])
def google_callback(request):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    service = build('gmail', 'v1', credentials=credentials)

    # Fetch messages
    result = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = result.get('messages', [])

    saved_emails = []
    for msg in messages:

        
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_detail['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        snippet = msg_detail.get('snippet', '')



        # Extract data (logic from your previous code)
        # ...
        
        # Save or Update in database

        email_obj, created = EmailMessage.objects.update_or_create(
            gmail_id=msg['id'],
            defaults={
                'subject': subject,
                'sender': sender,
                'snippet': snippet,
                'body': msg_detail.get('snippet') # Or parse full body
            }
        )
        saved_emails.append({
            "id": email_obj.id,
            "subject": email_obj.subject,
            "sender": email_obj.sender,
            "snippet": email_obj.snippet
        })

    return Response(saved_emails)

def fetch_emails(request):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        return HttpResponse("No valid credentials. Please log in first.")
    service = build('gmail', 'v1', credentials=creds)

    try:
        results = service.users().messages().list(userId='me', maxResults=5).execute()
        messages = results.get('messages', [])

        email_subjects = []
        if not messages:
            email_subjects.append('No messages found.')
        else:
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                snippet = msg.get('snippet', '(No snippet)')
                email_subjects.append(snippet)
        return HttpResponse('<br><br>'.join(email_subjects))
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
    

@api_view(['POST']) 
def summarize_email(request,pk):
    email = EmailMessage.objects.get(pk=pk)
    
    if not email.summary:
        # Placeholder for AI logic (e.g., OpenAI/Gemini call)
        # ai_response = call_llm(email.body)
        email.summary = f"This is an AI summary for: {email.subject}" 
        email.save()
        
    return Response({"summary": email.summary})