from django.contrib import admin
from .models import Clients

# Register your models here.

class CLientsModelAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'matricula',)
    search_fields = ('nome',)

admin.site.register(Clients, CLientsModelAdmin)

