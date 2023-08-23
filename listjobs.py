import os
import openai

# Set your OpenAI API key
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# List fine-tuning jobs
response = openai.FineTuningJob.list(limit=10)  # This will list the latest 10 fine-tuning jobs

# Print the results
for job in response['data']:
    print(f"ID: {job['id']}, Model: {job['model']}, Created At: {job['created_at']}, Status: {job['status']}")

# Note: You can adjust the limit parameter to retrieve more or fewer jobs.
print(response)