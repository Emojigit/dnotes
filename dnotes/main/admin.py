from django.contrib import admin
from main import models, settings

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('tid','title','owner' )
    list_display_links = ('tid', )
    list_filter = ('owner', )

admin.site.register(models.Note,NoteAdmin)

admin.site.site_title = settings.site_name

