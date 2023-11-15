from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title',) #The value of 'list_display' must be a list or tuple

admin.site.register(models.Entries, EntryAdmin)
