from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('course', 'id', 'status', 'slug', 'author', 'price')
    prepopulated_fields = {'slug': ('course',), }


admin.site.register(models.Category)
