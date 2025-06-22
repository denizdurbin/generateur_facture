from django.test import TestCase
from .models import Produit, Facture, LigneFacture
from django.urls import reverse
from decimal import Decimal

class ProduitModelTest(TestCase):
    def test_creation_produit(self):
        p = Produit.objects.create(nom="Test", prix=10.0, date_peremption="2030-01-01")
        self.assertEqual(p.nom, "Test")
        self.assertTrue(p.prix >= 0)

class FactureModelTest(TestCase):
    def test_total_calcul(self):
        p1 = Produit.objects.create(nom="Prod1", prix=10.0, date_peremption="2030-01-01")
        p2 = Produit.objects.create(nom="Prod2", prix=20.0, date_peremption="2030-01-01")
        facture = Facture.objects.create()
        LigneFacture.objects.create(facture=facture, produit=p1, prix_unitaire=p1.prix)
        LigneFacture.objects.create(facture=facture, produit=p2, prix_unitaire=p2.prix)
        self.assertEqual(facture.total(), Decimal('30.0'))

class VueFactureTest(TestCase):
    def setUp(self):
        self.p1 = Produit.objects.create(nom="Prod1", prix=10.0, date_peremption="2030-01-01")
        self.p2 = Produit.objects.create(nom="Prod2", prix=20.0, date_peremption="2030-01-01")

    def test_creer_facture_post(self):
        response = self.client.post(reverse('creer_facture'), {'produits': [self.p1.id, self.p2.id]})
        self.assertEqual(response.status_code, 302)  # vers detail
        facture = Facture.objects.first()
        self.assertIsNotNone(facture)
        self.assertEqual(facture.lignes.count(), 2)
