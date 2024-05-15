from django.shortcuts import render, get_object_or_404
from django.views import generic
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
    cars_all = Automobilis.objects.all()
    return render(request, 'cars.html', {'cars_all': cars_all})


def get_one_car(request, car_id):
    car = get_object_or_404(Automobilis, pk=car_id)
    jobs = get_object_or_404(Uzsakymas, pk=car_id)
    context = {
        'car_obj': car,
        'jobs_obj': jobs
    }
    return render(request, 'car.html', context=context)


class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    context_object_name = 'uzsakymas_list'
    template_name = 'orders.html'


class UzsakymasDetailedView(generic.DetailView):
    model = Uzsakymas
    context_object_name = 'uzsakymas'
    template_name = 'order.html'


def get_all_current_orders_count(request):
    vykdomu_uzsakymai = Uzsakymas.objects.filter(status__exact='e').count()
    vykdomu_uzsakymai2 = Uzsakymas.objects.filter(status__exact='ap').count()

    vykdomu_uzsakymu_kiekis = vykdomu_uzsakymai + vykdomu_uzsakymai2

    uzsakymai1 = Uzsakymas.objects.filter(status__exact='e').all()
    usakymai2 = Uzsakymas.objects.filter(status__exact='ap').all()

    context = {
        'kiekis': vykdomu_uzsakymu_kiekis,
        'uzsakymai1': uzsakymai1,
        'uzsakymai2': usakymai2,
    }

    return render(request, 'curorders.html', context=context)


