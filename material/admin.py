from django.contrib import admin

from .models import Produto, Tipo, Material, Altura, Largura, Caract, Bitola_PEC, Bitola_CAB, Tipo_Forn, Unidade

admin.site.register(Produto)
admin.site.register(Tipo)
admin.site.register(Material)
admin.site.register(Altura)
admin.site.register(Largura)
admin.site.register(Caract)
admin.site.register(Bitola_PEC)
admin.site.register(Bitola_CAB)
admin.site.register(Tipo_Forn)
admin.site.register(Unidade)

