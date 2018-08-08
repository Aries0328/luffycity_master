from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class corsMiddleware(MiddlewareMixin):
    '''
    自定义中间件
    为响应增加响应头
    '''
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = settings.CORS_ALLOW_HEADERS
            response['Access-Control-Allow-Methods'] = settings.CORS_ALLOW_METHODS
        return response