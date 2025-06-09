import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

        logger.info("Request logging initialized")
    
    def __call__(self, request):

        response = self.get_response(request)

        user = request.user if request.user.is_authenticated else "Anonymous"

        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        return response