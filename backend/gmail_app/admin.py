from django.contrib import admin
from .models import EmailMessage

@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    # This makes the list view much more readable
    list_display = ('subject', 'sender', 'gmail_id')
    search_fields = ('subject', 'sender', 'body')