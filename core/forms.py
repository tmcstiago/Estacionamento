from django.forms import ModelForm
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalistas
)


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovRotForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalistas
        fields = '__all__'