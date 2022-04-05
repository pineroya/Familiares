from django.contrib import admin
from .models import Familymodel
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'fecha')

admin.site.register(Familymodel, FamiliaAdmin)