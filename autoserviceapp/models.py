import uuid

from django.db import models
from random import randint


def make_random_vin():
    return randint(100000000, 999999999)


# Create your models here.

class AutomobilioModelis(models.Model):
    marke = models.CharField('Marke', max_length=20)
    modelis = models.CharField('Modelis', max_length=20)
    metai = models.IntegerField('Metai')
    variklis = models.CharField('Variklis', max_length=3)

    def __str__(self):
        return f'{self.marke} {self.modelis} {self.metai} {self.variklis}'

    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilio modeliai'
        ordering = ['marke']


class Automobilis(models.Model):
    valstybinis_nr = models.CharField('Valstybinis Nr.', max_length=6)
    vin = models.IntegerField('VIN code', default=make_random_vin)
    klientas = models.CharField('Klientas', max_length=20)
    automobilio_modelis = models.ForeignKey(AutomobilioModelis, on_delete=models.CASCADE)  # check how works

    def __str__(self):
        return f'{self.valstybinis_nr} {self.vin} {self.klientas} {self.automobilio_modelis}'

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def modelis(self):
        return self.automobilio_modelis.modelis

    def marke(self):
        return self.automobilio_modelis.marke


class Uzsakymas(models.Model):
    data = models.DateField('Data', blank=True, null=True)
    suma = models.FloatField('Suma')
    automobilis = models.ForeignKey(Automobilis, on_delete=models.CASCADE)

    CAR_STATUS = (
        ('p', 'Priimtas'),
        ('e', 'Eigoje'),
        ('ap', 'Atliktu darbu patikrinimas'),
        ('i', 'Ivykdytas')
    )

    status = models.CharField(
        max_length=2,
        choices=CAR_STATUS,
        blank=True,
        default='a',
        help_text='Uzsakymo statusas'
    )

    def __str__(self):
        return f'{self.data} {self.suma} {self.automobilis}'

    class Meta:
        verbose_name = 'Uzsakymas'
        verbose_name_plural = 'Uzsakymai'




    def modelis(self):
        return self.automobilis.automobilio_modelis.modelis

    def marke(self):
        return self.automobilis.automobilio_modelis.marke

    def klientas(self):
        return self.automobilis.klientas


class UzsakymoEilutes(models.Model):
    kiekis = models.IntegerField('Kiekis')
    kaina = models.FloatField('Kaina')
    uzsakymas = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE)
    paslauga = models.ForeignKey('Paslauga', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.kiekis} {self.kaina}€'

    class Meta:
        verbose_name = 'Uzsakymo Eilute'
        verbose_name_plural = 'Uzsakymo Eilutes'


class Paslauga(models.Model):
    pavadinimas = models.CharField('pavadinimas', max_length=50)
    kaina = models.FloatField('Kaina')

    def __str__(self):
        return f'Paslauga: {self.pavadinimas} Kaina: {self.kaina}€'

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'
