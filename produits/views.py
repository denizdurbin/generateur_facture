from django.shortcuts import render
from .models import Produit, Facture
from django.core.paginator import Paginator

produits_per_page = 10

def liste_produits(request):
    print("debug")
    produits = Produit.objects.all()
    paginator = Paginator(produits, produits_per_page)
    page = request.GET.get('page')
    produits_page = paginator.get_page(page)
    return render(request, 'produits/liste.html', {'produits': produits_page})

def creer_facture(request):
    if request.method == 'POST':
        ids = request.POST.getlist('produits')
        facture = Facture.objects.create()
        facture.produits.set(ids)
        return redirect('detail_facture', id=facture.id)
    produits = Produit.objects.all()
    return render(request, 'produits/creer_facture.html', {'produits': produits})

def detail_facture(request, id):
    facture = Facture.objects.get(id=id)
    return render(request, 'produits/detail_facture.html', {'facture': facture})