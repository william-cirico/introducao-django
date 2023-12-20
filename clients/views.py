from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client
from .forms import ClientForm

# Create your views here.
def index(request):
    # clients = Client.objects.all()
    clients = Client.objects.order_by("name")
    
    context = {
        "clients": clients
    }
    
    return render(request, 'index.html', context)


def detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    
    context = {
        "client": client
    }
    
    return render(request, 'detail.html', context)
    

def create(request):
    # Método POST -> Enviando o formulário de cadastro
    if request.method == "POST":
        form = ClientForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        
        context = {
            "form": form
        }
        
        return render(request, 'create.html', context)
    
    # Método GET -> Abrir a página para cadastrar
    form = ClientForm()
    
    context = {
        "form": form
    }
    
    return render(request, 'create.html', context)


def update(request, client_id):
    return HttpResponse(f"Edição: {client_id}")


def delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    
    return HttpResponseRedirect(reverse("index"))