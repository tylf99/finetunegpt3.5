import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTuningJob.create(training_file="file-J75w22sUMnSm4iT40kiyrm7", model="gpt-3.5-turbo-0613")