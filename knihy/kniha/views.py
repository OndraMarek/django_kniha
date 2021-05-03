from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    context = {
        'nadpis': 'Úvodní stránka',
        'obsah': 'Obsah stránky'
    }

    return render(request, template_name='index.html', context=context)


class KnihaListView(ListView):
    model = Knihy

    context_object_name = 'kniha_list'
    template_name = 'list.html'


class KnihaDetailView(DetailView):
    model = Knihy

    context_object_name = 'kniha'
    template_name = 'detail.html'


class KnihaCreate(CreateView):
    model = Knihy
    fields = ['nazev', 'popis', 'autor', 'rok', 'zanry', 'foto']
    initial = {'nazev': 'test'}


class KnihaUpdate(UpdateView):
    model = Knihy
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class KnihaDelete(DeleteView):
    model = Knihy
    success_url = reverse_lazy('list')