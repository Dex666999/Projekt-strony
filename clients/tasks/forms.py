from django import forms
from .models import Klient, Zadanie, Kategoria, Wiadomosc

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['nazwa', 'imie', 'nazwisko', 'email']

class ZadanieForm(forms.ModelForm):
    class Meta:
        model = Zadanie
        fields = ['nazwa', 'opis', 'klient', 'kategoria']
        widgets = {'kategoria': forms.HiddenInput(),
                   'klient': forms.HiddenInput()}

class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa', 'klient']
        widgets = {'klient': forms.HiddenInput()}

class WiadomoscForm(forms.ModelForm):
    class Meta:
        model = Wiadomosc
        fields = ['tekst', 'klient']
        widgets = {'klient': forms.HiddenInput()}
