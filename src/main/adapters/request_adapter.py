from typing import Callable
from fastapi import Request as RequestFastApi

def request_adapter(request: RequestFastApi, callback: Callable):
    ''' FastApi Adapter '''
    
    http_request = {
        'query_params': request.query_params,
        'body': request.json()
    }

    http_response = callback(http_request)
    return http_response
