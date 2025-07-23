from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'long_url', 'date_created', 'click_count')
    search_fields = ('long_url', 'short_code')
    list_filter = ('date_created',)