from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }
# Register your models here.


admin.site.register(Page, PageAdmin)
