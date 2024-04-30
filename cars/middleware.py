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
        
        if hasattr(request, 'resolver_match') and request.resolver_match is not None:
            view_func = request.resolver_match.func
            view_class = view_func.__self__ if hasattr(view_func, '__self__') else None

            if view_class:
                module = view_class.__module__
                filename = module + '.' + view_class.__name__
            else:
                module = view_func.__module__
                filename = module + '.' + view_func.__name__

        else:
            filename = ''

        request_info['filename'] = filename
       

      
        with open('request_logs.txt', 'a') as f:
            f.write(str(request_info) + '\n')

        return response