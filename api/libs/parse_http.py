import json

def parse_http_post(request):
    try:
        return request.json
    except Exception as exc:
        print(exc)
        return None
    
def parse_http_get(request):
    try:
        return request.args
    except Exception as exc:
        print(exc)
        return None