import openai

class ChatService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.chat_history = []

    def get_response(self, prompt):
        self.chat_history.append({"role": "user", "content": prompt})

        # Prepare chat messages in the required format for OpenAI API
        messages = self.chat_history.copy()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            max_tokens=1000,
            temperature=0.8
        )

        ai_reply = response.choices[0].message["content"]
        self.chat_history.append({"role": "ai", "content": ai_reply})
        
        return ai_reply
