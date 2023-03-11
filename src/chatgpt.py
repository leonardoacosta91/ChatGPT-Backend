import openai
import requests
import os
import json


class ChatGPT:
    def __init__(self):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.openai = openai
        self.openai.api_key = os.getenv("OPENAI_APIKEY")

    def send_message(self, message):
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"{message}",
                }
            ],
            "temperature": 1.0,
            "top_p": 1.0,
            "n": 1,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai.api_key}",
        }

        response = requests.post(self.url, headers=headers, json=payload, stream=False)
        json_response = json.loads(response.text)
        return json_response
