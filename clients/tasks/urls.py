from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.lista_klientow, name='lista_klientow'),
    path('<int:klient_id>/', views.lista_zadan, name='lista_zadan'),
    path('nowy_klient/', views.nowy_klient, name='nowy_klient'),
    path('<int:klient_id>/<int:kategoria_id>/nowe_zadanie/', views.nowe_zadanie, name='nowe_zadanie'),
    path('<int:klient_id>/<int:kategoria_id>/<int:zadanie_id>/usun_zadanie/', views.usun_zadanie, name='usun_zadanie'),
    path('<int:klient_id>/nowa_kategoria/', views.nowa_kategoria, name='nowa_kategoria'),
    path('<int:klient_id>/<int:kategoria_id>/usun_kategorie/', views.usun_kategorie, name='usun_kategorie'),
    path('<int:klient_id>/wiadomosci/', views.wiadomosc_lista, name='wiadomosci'),
    path('<int:klient_id>/wiadomosci/nowa_wiadomosc/', views.nowa_wiadomosc, name='nowa_wiadomosc'),

]