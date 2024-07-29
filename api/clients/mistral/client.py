from mistral.client import MistralClient

def init_mistral_client(api_key):
    return MistralClient(api_key=api_key)