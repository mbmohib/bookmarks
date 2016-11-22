from django.contrib import admin

from .models import Catagory, UrlPost


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', )

class UrlPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'updated')
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(UrlPost, UrlPostAdmin)
