from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Facture, LigneFacture
from .forms import ProduitForm
from django.core.paginator import Paginator

produits_per_page = 10

def liste_produits(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, produits_per_page)
    page = request.GET.get('page')
    produits_page = paginator.get_page(page)
    return render(request, 'produits/liste_produits.html', {'produits': produits_page})

def creer_facture(request):
    if request.method == 'POST':
        ids = request.POST.getlist('produits')
        facture = Facture.objects.create()
        for produit_id in ids:
            produit = Produit.objects.get(id=produit_id)
            LigneFacture.objects.create(
                facture=facture,
                produit=produit,
                prix_unitaire=produit.prix
            )
        return redirect('detail_facture', id=facture.id)
    produits = Produit.objects.all()
    return render(request, 'produits/creer_facture.html', {'produits': produits})


def detail_facture(request, id):
    facture = get_object_or_404(Facture, id=id)
    return render(request, 'produits/detail_facture.html', {'facture': facture})

def creer_produit(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'produits/form_produit.html', {'form': form})

def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'produits/form_produit.html', {'form': form})

def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'produits/confirm_supprimer.html', {'produit': produit})

def liste_factures(request):
    factures = Facture.objects.all()
    return render(request, 'produits/liste_factures.html', {'factures': factures})

def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'produits/confirm_supprimer_facture.html', {'facture': facture})
