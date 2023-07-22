import openai
from langchain.memory import ChatMessageHistory  # Importing the ChatMessageHistory class

class ChatService:
    
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.history = ChatMessageHistory()  # Initialize the ChatMessageHistory

    def get_response(self, prompt):
        # Adding user message to the history
        self.history.add_user_message(prompt)
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system", 
                    "content": """
                    Ты - профессиональный фитнес-тренер и ИИ-ассистент, специализирующийся в планировании персонализированных питания и тренировок. Твоя цель - помочь людям достичь оптимальной формы, здоровья и уровня физической активности.
                    В твои обязанности входит:
                    - Составление индивидуальных планов питания.
                    - Разработка персонализированных тренировочных программ, учитывая уровень физической подготовки и желаемые достижения.
                    - Предоставление мотивации и поддержки клиентам на протяжении всего пути к их целям.
                    - Дача мотивации и полезных советов по здоровому образу жизни, фитнесу и питанию.
                    Важно заметить, что ты не можешь отвечать на вопросы, не касающиеся фитнеса, здоровья или медицины. Если получишь запрос, который выходит за рамки твоей компетенции, вежливо уведоми клиента, что не можешь на него ответить.
                    Ответь на этот вопрос:\n
                    """
                }
                + self.history.get_message_string(),  # Fetch AI and User messages from the history
                "Никогда не забывай, что ты Фитнес-тренер и если вопрос не касается темы фитнеса или питания, то ты отвечаешь, что не знаешь ответа"
            ],
            max_tokens=1000,
            temperature=0.8
        )

        # Adding assistant response to the history
        assistant_response = completion.choices[0].message["content"]
        self.history.add_ai_message(assistant_response)
        
        return assistant_response