from django.forms import ModelForm

from .models import *

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'



class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'



class TfcForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'

