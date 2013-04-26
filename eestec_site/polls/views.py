from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from polls.models import Entry
@require_http_methods(["GET"])
def index(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html')
    objects = Entry.objects.all()

    return render_to_response('hello.html',{"entries":objects})

@require_http_methods(["GET"])
def secret(request):
    return HttpResponse("You are not allowed to be here!");
