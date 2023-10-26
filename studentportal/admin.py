from django.contrib import admin
from.models import notes
# Register your models here.

class shownotes(admin.ModelAdmin):
    list_display = ['user','title','desc']
admin.site.register(notes,shownotes)