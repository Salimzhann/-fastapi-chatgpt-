import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

class ChatService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.conversation = ConversationChain(llm=ChatOpenAI(), memory=ConversationBufferMemory(), verbose=True)
        self.messages = []

    def get_response(self, prompt):
        user_message = {"role": "user", "content": prompt}
        self.messages.append(user_message)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=self.messages,
            max_tokens=1000,
            temperature=0.8
        )

        ai_reply = completion.choices[0].message["content"]
        ai_message = {"role": "ai", "content": ai_reply}
        self.messages.append(ai_message)

        return ai_reply

