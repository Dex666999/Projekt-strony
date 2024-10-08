from django.contrib import admin
from .models import Klient, Zadanie, Kategoria, Wiadomosc

admin.site.register(Klient)
admin.site.register(Zadanie)
admin.site.register(Kategoria)
admin.site.register(Wiadomosc)
