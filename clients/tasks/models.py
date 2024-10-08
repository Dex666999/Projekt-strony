from django.db import models

class Klient(models.Model):
    nazwa = models.CharField(max_length=100,)
    imie = models.CharField(max_length=100, null=True, default="")
    nazwisko = models.CharField(max_length=100, null=True, default="")
    opis = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nazwa

class Kategoria(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Zadanie(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()

    def __str__(self):
        return self.nazwa

class Wiadomosc(models.Model):
    tekst = models.TextField(blank=False)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    czas = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tekst
