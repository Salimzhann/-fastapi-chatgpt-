import openai

class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.messages = []
        self.last_user_request = None
        self.last_ai_response = None

    def get_response(self, prompt):
        if self.last_user_request is not None:
            self.messages.append({"role": "user", "content": self.last_user_request})
        if self.last_ai_response is not None:
            self.messages.append({"role": "system", "content": self.last_ai_response})

        self.messages.append({"role": "user", "content": prompt})
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=self.messages,
            max_tokens=1000, 
            temperature=0.8 
        )
        
        response = completion.choices[0].message
        self.messages.append({"role": "system", "content": response})

        self.last_user_request = prompt
        self.last_ai_response = response
        
        return response
