from django.shortcuts import render
from dashboard.models import *


def home(request):
    dataset = Dataset.objects.all()
    context = {}
    return render(request, 'dashboard/home.html', context)


def statistics_page(request):
    context = {}
    return render(request, 'dashboard/statistics.html', context)
