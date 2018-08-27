from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PessoaForm, VeiculoForm
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalistas,
)


def home (request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def lista_mov_rotativos(request):
    mov_rot = MovRotativo.objects.all()
    return render(request, 'core/lista_mov_rotativos.html', {'mov_rotativos': mov_rot})


def lista_mov_mensalistas(request):
    mov_mensalistas = MovMensalistas.objects.all()
    return render(request, 'core/lista_mov_mensalistas.html', {'mov_mensalistas': mov_mensalistas})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})