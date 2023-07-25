import openai

class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.conversation_memory = []

    def get_response(self, prompt):
        # Append the user's message to the conversation memory
        self.conversation_memory.append({"role": "user", "content": prompt})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=self.conversation_memory,  # Pass the entire conversation history
            max_tokens=1000, 
            temperature=0.8 
        )

        # Append the AI's reply to the conversation memory
        self.conversation_memory.append({"role": "system", "content": completion.choices[0].message})

        return completion.choices[0].message
