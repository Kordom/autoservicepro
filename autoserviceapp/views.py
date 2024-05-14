from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def index(request):
    paslaugu_kiekis = Paslauga.objects.count()
    uzsakymu_kiekis = Uzsakymas.objects.count()
    atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(status__exact='i').count()
    automobiliu_kiekis = Automobilis.objects.count()

    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis
    }

    return render(request, 'index.html', context=context)


def show_all_cars(request):
    cars_all = AutomobilioModelis.objects.all().order_by('marke')
    return render(request, 'cars.html', {'cars_all': cars_all})


def get_one_car(request, car_id):
    car = get_object_or_404(Automobilis, pk=car_id)
    return render(request, 'car.html', {'car_obj': car})
