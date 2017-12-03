from django.contrib import admin

from .models import Recruitment,Interview,ArchiveList

admin.site.register(Recruitment)
admin.site.register(Interview)
admin.site.register(ArchiveList)