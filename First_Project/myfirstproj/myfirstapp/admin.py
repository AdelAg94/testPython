from django.contrib import admin
from myfirstapp.models import Topic,WebPage,AccessRecord,PersonProfile

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(PersonProfile)