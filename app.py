import json
import requests
import os
# Prepare and save data (assuming 'data' variable is defined somewhere above)
data = []
with open('/Users/tylerf/Documents/coding projects/finetune3.5/tinder_dataset.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line))

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

# Upload the file to OpenAI
with open('/Users/tylerf/Documents/coding projects/finetune3.5/tinder_dataset.jsonl', 'rb') as file:
    files = {
        'file': ('/Users/tylerf/Documents/coding projects/finetune3.5/tinder_dataset.jsonl', file),
    }

    response = requests.post(
        "https://api.openai.com/v1/files",
        headers=headers,
        data={"purpose": "fine-tune"},
        files=files
    )
    print(response.text)
    response.raise_for_status()  # Raise an exception for HTTP errors
    file_id = response.json().get("id")