import requests
from datetime import datetime
import os

# GitHub Secrets లో save చేసిన webhook URL
webhook_url = os.environ.get("WEBHOOK_URL")

# Current date in DD/MM/YYYY format
today = datetime.now().strftime("%d/%m/%Y")
message = f"Task updates: {today}"

# Prepare JSON data
data = {
    "message": message
}

# Send POST request to Chatspace
response = requests.post(webhook_url, json=data)
print(response.text)
