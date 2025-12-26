# backend/gmail_app/serializers.py
from rest_framework import serializers
from .models import EmailMessage

class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = '__all__' # This includes subject, sender, body, and summary