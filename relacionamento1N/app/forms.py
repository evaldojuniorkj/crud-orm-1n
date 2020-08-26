from django.forms import ModelForm
from .models import Marca
from .models import Produto


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'categoria']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'marca']


