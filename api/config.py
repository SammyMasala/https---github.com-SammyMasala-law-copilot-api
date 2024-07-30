import os

# SYSTEM
NODE_ENV = os.environ.get("NODE_ENV", "staging")

# AWS
AWS_REGION = os.environ.get("AWS_REGION", "ap-southeast-1")

# MISTRAL
MODEL_NAME = os.environ.get("MODEL_NAME", "open-mixtral-8x22b")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "example-api-key")

# DYNAMODB
TABLE_NAME = os.environ.get("TABLE_NAME", "sessions-table-test")