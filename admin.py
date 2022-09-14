from django.contrib import admin

from . models import Catalogues, Size

class CataloguesA(admin.ModelAdmin):
    list_display = ('fulltitle','consnumber')
    
class SizeA(admin.ModelAdmin):
    list_display = ('id', 'booksize')

admin.site.register(Catalogues, CataloguesA)
admin.site.register(Size, SizeA)

# Register your models here.
