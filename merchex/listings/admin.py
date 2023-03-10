from django.contrib import admin

from  listings.models import Band, Resources, Category

# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')
    prepopulated_fields = {"slug": ("category", "name")}

admin.site.register(Category)
admin.site.register(Band, BandAdmin)
admin.site.register(Resources)
