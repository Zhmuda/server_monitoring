from django.http import HttpResponseForbidden

class SimpleAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Access denied")
        return self.get_response(request)