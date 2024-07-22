import json


def parse_http_post(request):
    try:
        return json.loads(request.data)
    except Exception as exc:
        print(exc)
        return None
    
def parse_http_get(request):
    try:
        return json.loads(request.params)
    except Exception as exc:
        print(exc)
        return None