from django.contrib import admin

from . models import Catalogues

class CataloguesA(admin.ModelAdmin):
    list_display = ('fulltitle','consnumber')

admin.site.register(Catalogues, CataloguesA)

# Register your models here.
