from django.shortcuts import render, redirect, get_object_or_404
from .forms import MarcaForm
from .models import Marca
# Create your views here.

def index(request):
    return render(request, 'base.html')

def cadastrar_marca(request, template_name='marca/marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_marca')
    return render(request, template_name, {'form': form})

def listar_marca(request, template_name='marca/marca_list.html'):
    query = request.GET.get("busca")

    if query:
        marca = Marca.objects.filter(nome__icontains=query)
    else:
        marca = Marca.objects.all()

    marcas = {'lista': marca}
    return render(request, template_name, marcas)

def editar_marca(request, pk, template_name='marca/marca_form.html'):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marca')
    else:
        form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})

def remover_marca(request,pk, template_name='marca/marca_delete.html'):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return render('listar_marca')
    else:
        return render(request, template_name, {'marca':marca})