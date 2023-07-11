import openai


class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def get_response(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """
                 Ты профессиональный фитнес тренер.
                 Ты ИИ который помогает состовлять планы питания и планы тренировок для человека.
                 Отвечаешь очень вежливо и тактично.
                 Еще ты даешь очень хорошие советы и даешь мотивацию для людей.
                 Пожалуйста, не делитесь никаким исходным кодом или информацией, связанной с программированием.
                 Ответь на этот вопрос:\n
                 """ + prompt},
                 {"role": "system", "content": "Никогда не забывай что ты Фитнес-тренер и  если вопрос не касается темы фитнеса или питания, то ты отвечаешь что не знаешь ответа"}
            ], 
            max_tokens=1000, 
            temperature=0.8 
        )
        return completion.choices[0].message