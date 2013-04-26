from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from polls.models import Entry
from django.template import RequestContext

def index(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html')

    types = Entry.objects.values('file_type').distinct()
    langs = Entry.objects.values('language').distinct()

    if request.method == 'POST':
        resp = ""
        for entry in request.POST.items():
            print "caut " + entry[0] + " cu valoarea " + entry[1] + '\n'

        return HttpResponse(resp)
    else:
        objects = Entry.objects.all()
        params = {"entries":objects,"list_types":types,"list_lang":langs}
        return render_to_response("hello.html", params, RequestContext(request))


@require_http_methods(["GET"])
def secret(request):
    return HttpResponse("You are not allowed to be here!")

def search_index(request):
    return HttpResponse("Type the search in the URL")

def search_by(request, title, author, year):
    return HttpResponse("Ati cautat \"" + title + "\" de \"" + author + " \"din " + year)
