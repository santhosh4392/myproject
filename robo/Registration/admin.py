from django.contrib import admin
from .models import personal

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'Age', 'Address')
    search_fields = ('name', 'Age')

admin.site.register(personal)