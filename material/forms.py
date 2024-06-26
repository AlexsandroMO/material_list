from django import forms

from .models import Produto, Altura

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('produto',)


class AlturaForm(forms.ModelForm):
    class Meta:
        model = Altura
        fields = ('altura',)