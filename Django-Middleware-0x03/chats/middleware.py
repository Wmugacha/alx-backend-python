import logging
from datetime import datetime, time
from django.utils import timezone
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

        logger.info("Request logging initialized")
    
    def __call__(self, request):

        response = self.get_response(request)

        user = getattr(request, 'user', 'Anonymous')
        if user != 'Anonymous' and user.is_authenticated:
            user = str(user)
        else:
            user = 'Anonymous'
        logger.info(f"{timezone.now()} - User: {user} - Path: {request.path}")

        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.start_time = time(18, 0)
        self.end_time = time(21, 0)

        logger.info(f"Time based access is in place: {self.start_time} to {self.end_time}")

    def is_time_allowed(self, current_time):
        return self.start_time <= current_time <= self.end_time

    def __call__(self, request):
        current_time = timezone.now().time()

        if not self.is_time_allowed(current_time):
            logger.warning(f"Access denied at {current_time} - Outside allowed hours")
            return HttpResponseForbidden("Access denied: Outside allowed timeframe")
        else:
            logger.debug(f"Granted access at: {current_time}")
            return self.get_response(request)