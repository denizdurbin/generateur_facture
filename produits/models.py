from django.db import models
from django.core.validators import MinValueValidator

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

#Represente une ligne de facture associant un prodit a une facture
#le prix est figé au moment de la creation
class LigneFacture(models.Model):
    facture = models.ForeignKey('Facture', on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.produit.nom} ({self.prix_unitaire}€) — Facture #{self.facture.id}"

class Facture(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit)

    def total(self):
        return sum(ligne.prix_unitaire for ligne in self.lignes.all())

    def __str__(self):
        return f"Facture {self.id} du {self.date.strftime('%d/%m/%Y')}"