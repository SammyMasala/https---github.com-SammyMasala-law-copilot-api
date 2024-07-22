import os
from api.libs.aws_sm import get_secret

TABLE_NAME = os.environ.get("TABLE_NAME", "sessions-table-test")
API_KEY = get_secret("MISTRAL_API_KEY") or "test_key"