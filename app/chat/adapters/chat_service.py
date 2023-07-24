import openai

class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.questions = []
        self.messages = []

    def get_response(self, prompt):
        # self.messages.append({"role": "user", "content": prompt})
        if len(self.questions) == 0:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=prompt,
                max_tokens=1000, 
                temperature=0.8 
            )
        else:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=f'last question: {self.questions[-1]} last answer: {self.messages[-1]}. current question: {prompt}',
                max_tokens=1000, 
                temperature=0.8 
            )

        self.questions.append(prompt)
        response = completion['choices'][0]['message']['content']
        self.messages.append(response)
        
        return response
