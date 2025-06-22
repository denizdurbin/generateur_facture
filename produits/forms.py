from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'date_peremption': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d' 
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_peremption'].input_formats = ['%Y-%m-%d']