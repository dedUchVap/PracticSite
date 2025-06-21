from django.contrib import admin
from .models import Land

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'location', 'land_type')
    search_fields = ('title', 'location', 'land_type')
    list_filter = ('land_type',)
