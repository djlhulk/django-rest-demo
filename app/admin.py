from django.contrib import admin
from app.models import Place

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
	list_display = ('user','title', 'description','photo',)

admin.site.register(Place, PlaceAdmin)