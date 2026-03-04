import requests

# URL of the Django chatbot API endpoint
URL = "http://127.0.0.1:8000/chat/"

# Display instructions for the user
print("Terminal Chat Client (type 'quit' to exit)\n")

# Continuous loop to allow ongoing conversation with the chatbot
while True:
    
    # Prompt the user for input and remove extra spaces
    message = input("You: ").strip()

    # Allow the user to exit the chatbot
    if message.lower() in {"quit", "exit"}:
        break

    try:
        # Send the user's message to the Django chatbot API
        # The message is sent as JSON data
        response = requests.post(URL, json={"message": message}, timeout=10)

        # Attempt to parse the response as JSON
        try:
            data = response.json()

        except Exception:
            # If the server response is not valid JSON, print debugging information
            print("Server did not return JSON.")
            print("Status:", response.status_code)
            print("Content-Type:", response.headers.get("Content-Type"))
            print("Body (first 300 chars):")
            print(response.text[:300])
            continue

        # If the JSON response contains a chatbot reply, display it
        if "reply" in data:
            print("Bot:", data["reply"])
        else:
            # If JSON exists but doesn't contain expected reply field
            print("Server JSON:", data)

    except requests.exceptions.RequestException as e:
        # Handle connection errors such as server not running
        print("Request error:", e)