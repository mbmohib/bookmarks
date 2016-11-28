from django.contrib import admin

from .models import Category, UrlPost


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'updated', )


class UrlPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'category', 'updated')
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(UrlPost, UrlPostAdmin)
