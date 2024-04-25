import time
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        
        request_info = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'path': request.path,
            'method': request.method,
            'response_time': end_time - start_time  
        }

      
        with open('request_logs.txt', 'a') as f:
            f.write(str(request_info) + '\n')

        return response