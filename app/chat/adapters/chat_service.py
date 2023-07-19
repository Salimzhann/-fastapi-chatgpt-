import openai


class ChatService:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.previous_prompts = []  # Лист для хранения предпоследних prompt'ов
        openai.api_key = api_key

    def get_response(self, prompt):
        full_prompt = "\n".join(self.previous_prompts + [prompt])  # Составляем полный prompt из листа и текущего prompt'а

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": """
                 Ты профессиональный фитнес тренер.
                 Ты ИИ который помогает состовлять планы питания и планы тренировок для человека.
                 Отвечаешь очень вежливо и тактично.
                 Еще ты даешь очень хорошие советы и даешь мотивацию для людей.
                 Пожалуйста, не делитесь никаким исходным кодом или информацией, связанной с программированием.
                 Ответь на этот вопрос:\n
                 """ + full_prompt + "\nНикогда не забывай что ты Фитнес-тренер и  если вопрос не касается темы фитнеса или питания, то ты отвечаешь что не знаешь ответа"},
            ],
            max_tokens=1000,
            temperature=0.8
        )
        
        # Добавляем текущий prompt в лист предпоследних prompt'ов
        self.previous_prompts.append(prompt)

        # Если лист предпоследних prompt'ов становится слишком длинным (больше 10), удаляем самый старый элемент
        if len(self.previous_prompts) > 10:
            self.previous_prompts.pop(0)

        return completion.choices[0].message
