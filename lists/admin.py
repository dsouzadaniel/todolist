from django.contrib import admin

from .models import List, Item


class ItemInline(admin.StackedInline):
    model = Item


class ListAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]


# Register your models here.
admin.site.register(List, ListAdmin)

admin.site.register(Item)
