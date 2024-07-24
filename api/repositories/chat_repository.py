from mistralai.client import MistralClient

class ChatRepository:
    def chat_response(self, client: MistralClient, model, messages):
        response = client.chat(model=model, messages=messages)
        return response.choices[0].message.content

