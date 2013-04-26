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
    types = Entry.objects.values('file_type').distinct()
    return render_to_response('hello.html',{"entries":objects,"list_types":types})

@require_http_methods(["GET"])
def secret(request):
    return HttpResponse("You are not allowed to be here!")

def search_index(request):
    return HttpResponse("Type the search in the URL")

def search_by(request, title, author, year):
    return HttpResponse("Ati cautat \"" + title + "\" de \"" + author + " \"din " + year)
