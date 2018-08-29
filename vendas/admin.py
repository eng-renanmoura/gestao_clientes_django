from django.contrib import admin
from .models import Venda, ItemDoPedido
from .actions import nfe_emitida

# Register your models here.
class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    list_filter = ('pessoa__doc', 'desconto')
    autocomplete_fields = ['pessoa']
    #raw_id_fields = ('pessoa',)
    list_display = ('id', 'pessoa', 'nfe_emitida')
    actions = [nfe_emitida]
    #filter_horizontal = ['produtos',]
    inlines = [ItemPedidoInline]

    def get_total(self, obj):
        return obj.get_total()

    get_total.short_description = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)