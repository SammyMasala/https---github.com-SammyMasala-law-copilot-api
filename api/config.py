import os

# SYSTEM
NODE_ENV = os.environ.get("NODE_ENV", "staging")

# AWS
AWS_REGION = os.environ.get("AWS_REGION", "ap-southeast-1")

# MISTRAL
SYSTEM_PROMPT_LAW = """
                PROMPT: Provide me concise notes about the given prompt in UK Law. In a response less than 300 words, give the following if known: 
                - subject: The subject of the prompt in question. 
                - is_law: return 'yes' if this is a legal question, 'no' if not.
                - type: the type of the subject. Choose from the following: Case Law, Legislation, Legal Topic, Academic Article,
                - key_questions: Give a numbered list of the legal issues discussed by the prompt's subject. The list should be a string with a newline as a delimiter,
                - conclusions: Give a numbered list of the main takewaways from the subject. The list should be a string with a newline as a delimiter,
                - important_quotes: Give a numbered list of important quotes and their source related to the subject. The list should be a string with a newline as a delimiter,

                OUTPUT: Return your response as a JSON Object
                """
MODEL_NAME = os.environ.get("MODEL_NAME", "open-mixtral-8x22b")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "example-api-key")

# DYNAMODB
TABLE_NAME = os.environ.get("TABLE_NAME", "sessions-table-test")