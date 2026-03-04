import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot("DjangoBot")

# Custom responses
trainer = ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hi! Nice to meet you.",

    "What is your name?",
    "My name is DjangoBot.",

    "Who created you?",
    "I was created by Priya using Django and ChatterBot.",

    "What is this project?",
    "This is a terminal chatbot built using Django."
])

# Optional: train with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        response = chatbot.get_response(message)

        return JsonResponse({"reply": str(response)})

    return JsonResponse({"error": "POST request required"})