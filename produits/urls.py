from django.urls import path
from . import views

def test_view(request):
    return HttpResponse("Route test OK")
    
urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('facture/', views.creer_facture, name='creer_facture'),
    path('facture/<int:id>/', views.detail_facture, name='detail_facture'),
]