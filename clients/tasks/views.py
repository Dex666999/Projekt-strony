from django.shortcuts import render, redirect, get_object_or_404
from .models import Klient, Zadanie, Kategoria, Wiadomosc
from .forms import KlientForm, ZadanieForm, KategoriaForm, WiadomoscForm

def nowy_klient(request):
    if request.method == 'POST':
        form = KlientForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('lista_klientow')
    else:
        form = KlientForm()
    return render(request, 'nowy_klient.html', {'form': form})

def lista_klientow(request):
    klienci = Klient.objects.all()
    return render(request, 'lista_klientow.html', {'klienci': klienci},)

def lista_zadan(request, klient_id):
    klient = Klient.objects.get(id=klient_id)
    kategorie = klient.kategoria_set.all()
    return render(request, 'lista_zadan.html', {'klient': klient, 'kategorie': kategorie})

def nowe_zadanie(request, kategoria_id, klient_id):
    klient = Klient.objects.get(pk=klient_id)
    kategoria = Kategoria.objects.get(pk=kategoria_id)

    if request.method == 'POST':
        form = ZadanieForm(request.POST)
        if form.is_valid():
            zadanie = form.save(commit=False)
            zadanie.kategoria = kategoria
            zadanie.klient = klient
            zadanie.save()

            return redirect('lista_zadan', klient_id=klient_id)
    else:
        form = ZadanieForm()
    form.fields['kategoria'].initial = kategoria
    form.fields['klient'].initial = klient
    return render(request, 'nowe_zadanie.html', {'form': form, 'klient': klient, 'kategoria': kategoria})

def usun_zadanie(request, klient_id, kategoria_id, zadanie_id):
    zadanie = get_object_or_404(Zadanie, klient_id=klient_id, kategoria_id=kategoria_id, pk=zadanie_id)
    if request.method =="POST":
        zadanie.delete()
        return redirect('lista_zadan', klient_id=klient_id)
    return render(request, 'usun_zadanie.html', {'zadanie': zadanie})

def nowa_kategoria(request, klient_id):
    klient = Klient.objects.get(pk=klient_id)

    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            kategoria = form.save(commit=False)
            kategoria.klient = klient
            kategoria.save()

            return redirect('lista_zadan', klient_id = klient_id)
    else:
        form = KategoriaForm()
    form.fields['klient'].initial = klient
    return render(request, 'nowa_kategoria.html', {'form': form, 'klient': klient})

def usun_kategorie(request, klient_id, kategoria_id):
    kategoria = get_object_or_404(Kategoria, klient_id = klient_id, pk = kategoria_id)
    if request.method == "POST":
        kategoria.delete()
        return redirect('lista_zadan', klient_id = klient_id)
    return render(request, 'usun_kategorie.html', {'kategoria': kategoria})

def wiadomosc_lista(request, klient_id):
    wiadomosci = Wiadomosc.objects.all()
    klient = get_object_or_404(Klient, pk=klient_id)
    return render(request, 'chat.html', {'wiadomosci': wiadomosci, 'klient': klient})

def nowa_wiadomosc(request, klient_id):
    klient = Klient.objects.get(pk=klient_id)

    if request.method == 'POST':
        form = WiadomoscForm(request.POST)
        if form.is_valid():
            wiadomosc = form.save(commit=False)
            wiadomosc.klient = klient
            wiadomosc.save()

            return redirect('wiadomosci', klient_id=klient_id)
    else:
        form = WiadomoscForm()
    form.fields['klient'].initial = klient
    return render(request, 'nowa_wiadomosc.html', {'form': form, 'klient': klient})