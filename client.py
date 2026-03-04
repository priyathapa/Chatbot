import requests

URL = "http://127.0.0.1:8000/chat/"

print("Terminal Chat Client (type 'quit' to exit)\n")

while True:
    message = input("You: ").strip()
    if message.lower() in {"quit", "exit"}:
        break

    try:
        response = requests.post(URL, json={"message": message}, timeout=10)

        # If server didn't return JSON, print debug info
        try:
            data = response.json()
        except Exception:
            print("Server did not return JSON.")
            print("Status:", response.status_code)
            print("Content-Type:", response.headers.get("Content-Type"))
            print("Body (first 300 chars):")
            print(response.text[:300])
            continue

        if "reply" in data:
            print("Bot:", data["reply"])
        else:
            print("Server JSON:", data)

    except requests.exceptions.RequestException as e:
        print("Request error:", e)