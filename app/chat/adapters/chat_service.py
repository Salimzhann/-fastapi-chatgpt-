import openai

class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.messages = []

    def get_response(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=self.messages,
            max_tokens=1000, 
            temperature=0.8 
        )
        
        response = completion.choices[0].message
        self.messages.append({"role": "system", "content": response})
        
        return response
