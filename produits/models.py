from django.db import models
from django.core.validators import MinValueValidator

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit)

    def total(self):
        return sum(p.prix for p in self.produits.all())

    def __str__(self):
        return f"Facture {self.id} du {self.date.strftime('%d/%m/%Y')}"