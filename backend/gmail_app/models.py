from django.db import models

# Create your models here.
class EmailMessage(models.Model):
    gmail_id = models.CharField(max_length=255, unique=True)
    subject = models.TextField(null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    snippet = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
def __str__(self):
    return self.subject
