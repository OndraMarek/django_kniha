from django.forms import ModelForm
from .models import *


class KnihaForm(ModelForm):
    class Meta:
        model = Knihy
        fields = ['nazev', 'popis', 'autor', 'rok', 'zanry', 'foto','nakladatelstvi', 'isbn']