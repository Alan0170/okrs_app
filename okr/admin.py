from django.contrib import admin
from .models import Okr, Integrante


class InfoAdmin(admin.ModelAdmin):
    list_display = ['integrante', 'criado', 'atualizado']


admin.site.register(Okr, InfoAdmin)
admin.site.register(Integrante)
