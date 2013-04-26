from django.contrib import admin
from polls.models import Entry
from polls.models import Publisher
from polls.models import Published
admin.site.register(Entry)
admin.site.register(Publisher)
admin.site.register(Published)
