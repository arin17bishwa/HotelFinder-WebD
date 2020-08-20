from django.contrib import admin

# Register your models here.

from .models import Hotel,HotelSave

class HotelSaveAdmin(admin.TabularInline):
    model=HotelSave

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelSaveAdmin]
    #list_display = ['__str__']
    search_fields = ['name']
    class Meta:
        model=Hotel

admin.site.register(Hotel,HotelAdmin)
