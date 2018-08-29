from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Venda

# Create your views here.
class DashboardView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        data = {}
        data['media'] = Venda.objects.media()
        data['media_desconto'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_ped'] = Venda.objects.num_pedidos()
        data['n_ped_nfe'] = Venda.objects.num_pedidos_nfe()
        return render(request, 'vendas/dashboard.html', data)