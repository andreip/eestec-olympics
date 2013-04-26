from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse

@require_http_methods(["GET"])
def index(request):
    if not request.user.is_authenticated():
        return HttpResponse('Please login!')

    return HttpResponse("welcome, nigga!")
