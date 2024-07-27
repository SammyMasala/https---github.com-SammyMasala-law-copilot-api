import os
# AWS
AWS_REGION = os.environ.get("AWS_REGION", "ap-southeast-1")

# Sessions 
TABLE_NAME = os.environ.get("SESSIONS_TABLE", "sessions-table-test")

# Mistral GPT
CHAT_API_KEY = os.environ.get("MISTRAL_API_KEY", "test_key")
MODEL_NAME = os.environ.get("MODEL_NAME", "open-mixtral-8x22b")


