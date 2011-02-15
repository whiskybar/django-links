from django.contrib import admin
from links.models import Category, Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(Link, LinkAdmin)

