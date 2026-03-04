# Django Chatbot 
## Project Overview

This project implements a terminal-based chatbot using Django and ChatterBot. The chatbot allows users to send messages through a terminal client, which communicates with a Django backend API. The backend processes the message using the ChatterBot machine learning library and returns a response.

The goal of this project is to demonstrate how a Python terminal client can interact with a web-based chatbot service built with Django.

## Technologies Used

Python

Django

ChatterBot

SpaCy

Requests

PyYAML

# Project Structure
    Chatbot/
        manage.py
        client.py
        requirements.txt

        Chat/
            views.py
            urls.py

        Chatbot_project
            settings.py
            urls.py

    
# File Description

- manage.py: Django’s command-line utility used to run administrative tasks such as starting the server.

- client.py:  Terminal-based client that allows the user to chat with the chatbot.

- views.py: Contains the chatbot logic using the ChatterBot library.

- urls.py: Defines URL routes that connect the API endpoint to the chatbot view.

- requirements.txt:  Manifest file listing all Python dependencies required to run the project.

# Installation Instructions
1. Clone the repository
       `git clone https://github.com/priyathapa/Chatbot.git
       cd Chatbot`
   
2. Create a virtual environment
       `python -m venv venv`

   windows
       `venv\Scripts\activate`

   linux
       `source venv/bin/activate`

3. Install Dependencies
       `pip install -r requirements.txt`

4. Install the SpaCy language model
        `python -m spacy download en_core_web_sm`

# Running the application
Step 1: Start the Django server
    `python manage.py runserver`

Step 2: Run the terminal chatbot client
    `python client.py`
