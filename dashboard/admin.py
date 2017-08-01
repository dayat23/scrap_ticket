from django.contrib import admin
from .models import SiteScraping


class SiteScrapingAdmin(admin.ModelAdmin):
    list_display = ('scraping_site', 'periodicity')

# Register your models here.
admin.site.register(SiteScraping, SiteScrapingAdmin)
