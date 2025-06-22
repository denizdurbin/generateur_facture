from django.urls import path
from . import views

def test_view(request):
    return HttpResponse("Route test OK")

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('facture/', views.creer_facture, name='creer_facture'),
    path('facture/<int:id>/', views.detail_facture, name='detail_facture'),
    path('produit/ajouter/', views.creer_produit, name='creer_produit'),
    path('produit/<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produit/<int:pk>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
    path('factures/', views.liste_factures, name='liste_factures'),
    path('facture/<int:pk>/supprimer/', views.supprimer_facture, name='supprimer_facture'),
]