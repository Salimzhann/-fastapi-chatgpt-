from collections import deque
import openai

class ChatService:
    
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.chat_history = deque(maxlen=20)  # Initialize a deque with maximum length of 20

    def add_chat(self, role, content):
        self.chat_history.append({"role": role, "content": content})

    def get_response(self, user_message):
        self.add_chat("user", user_message)  # Add user message to the chat history

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=list(self.chat_history),  # Convert deque to a list for the OpenAI API
            max_tokens=1000,
            temperature=0.8
        )

        assistant_response = completion.choices[0].message['content']
        self.add_chat("assistant", assistant_response)  # Add GPT-3.5 response to the chat history
        return assistant_response