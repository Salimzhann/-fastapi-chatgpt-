import openai
from langchain.memory import ChatMessageHistory

class ChatService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.chat_history = ChatMessageHistory()

    def get_response(self, prompt):
        self.chat_history.add_user_message(prompt)

        # Prepare chat messages in the required format for OpenAI API
        messages = [{"role": "user", "content": msg.content} for msg in self.chat_history.messages]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            max_tokens=1000,
            temperature=0.8
        )

        ai_reply = completion.choices[0].message["content"]
        self.chat_history.add_ai_message(ai_reply)
        
        return ai_reply
