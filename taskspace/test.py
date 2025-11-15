import requests
from datetime import datetime
import os

# GitHub Secrets నుండి URL తీసుకుంటుంది
webhook_url = os.environ.get("WEBHOOK_URL")

if not webhook_url:
    raise ValueError("WEBHOOK_URL secret missing!")

# Current date in DD/MM/YYYY format
today = datetime.now().strftime("%d/%m/%Y")
message = f"Task updates: {today}"

# JSON payload for Google Chat
data = {"text": message}  # Google Chat expects "text"

# Send POST request to Chatspace
response = requests.post(webhook_url, json=data)
print(response.text)
