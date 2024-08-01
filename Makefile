start-local:
	python server.py

test-python:
	pytest

sls-dev:
	sls dev --region ap-southeast-1 --stage stg

sls-deploy-staging:
	sls deploy --region ap-southeast-1 --stage stg

sls-deploy-production:
	sls deploy --region ap-southeast-1 --stage prod