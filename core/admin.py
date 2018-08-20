from django.contrib import admin
from . import models
import math


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('__str__','checkin', 'checkout', 'valor_por_hora', 'pago','total')

    def valor_por_hora(self, object):
        return object.valor_hora.valor_hora
        


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'data_pagamento', 'total')


admin.site.register(models.Pessoa)
admin.site.register(models.Marca)
admin.site.register(models.Veiculo)
admin.site.register(models.Parametro)
admin.site.register(models.MovRotativo, MovRotativoAdmin)
admin.site.register(models.Mensalista)
admin.site.register(models.MovMensalistas, MovMensalistaAdmin)
