from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Person, Produto
from .forms import PersonForm
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

class PersonList(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'

class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')

class PersonDelete(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_cbv')

    #ideal usar o get abaixo caso seja necessario processar antes de retornar
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')

class ProdutoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maçã', 'Limão', 'Laranja', 'Pera', 'Melancia']
        lista_produtos = []
        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            lista_produtos.append(p)

        Produto.objects.bulk_create(lista_produtos)

        return HttpResponse('Funcionou')