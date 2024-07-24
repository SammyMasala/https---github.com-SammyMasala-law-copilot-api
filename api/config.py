import os
from api.libs.aws_sm import get_secret

# Sessions 
TABLE_NAME = os.environ.get("SESSIONS_TABLE", "sessions-table-test")

# Mistral GPT
CHAT_API_KEY = get_secret("MISTRAL_API_KEY") or "test_key"
CHAT_MODEL = "open-mixtral-8x22b"


