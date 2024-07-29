test-python:
	pytest

sls-deploy-staging:
	sls deploy --region ap-southeast-1 --stage stg

sls-deploy-production:
	sls deploy --region ap-southeast-1 --stage prod