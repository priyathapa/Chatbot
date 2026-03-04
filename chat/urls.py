from django.urls import path
from .views import chat_api  # Import the chat API view that handles chatbot requests

# URL patterns for the chat app
urlpatterns = [

    # When a request is made to "/chat/", Django will call the chat_api view
    # This endpoint receives user messages and returns the chatbot response
    path("chat/", chat_api),
]