from django.urls import path
from . import views

urlpatterns = [
    # OAuth Routes
    path('google/login/', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),

    # API Routes (used by React Axios calls)
    path('google/emails/', views.fetch_emails, name='fetch_emails_api'),
    path('google/summarize/<int:pk>/', views.summarize_email, name='summarize_email'),
]
