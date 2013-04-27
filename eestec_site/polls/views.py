import os

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from polls.models import Entry

def index(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html')

    types = Entry.objects.values('file_type').distinct()
    langs = Entry.objects.values('language').distinct()

    if request.method == 'POST':
        args = {}
        for entry in request.POST.items():
            if entry[1] != "":
                args[entry[0]] = entry[1]

        # Don't ask
        del args['csrfmiddlewaretoken']
        print args

        objects = Entry.objects.filter(**args)
        params = {"entries":objects, "list_types":types, "list_lang":langs}

        return render_to_response("hello.html", params, RequestContext(request))
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

def files(request, file_name):
    """
        Receive GET on /fiels and open the file locally if it
        exists, returning it to the user to be viewed in browser
        or to be saved locally.
    """
    path = os.path.join(settings.FILES_DIR, file_name)
    with open(path) as pdf:
        # Get entry extension from db.
        file_format = Entry.objects.get(file_name=file_name).format_type

        # Compose http response.
        response = HttpResponse(pdf.read(),
            mimetype="application/%s" % file_format)
        # The name to use for saving file.
        response['Content-Disposition'] = "inline;filename=%s" % file_name
        return response
