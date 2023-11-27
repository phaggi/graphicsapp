import datetime

from django.db.models import Count
from django.shortcuts import render
from qsstats import QuerySetStats

from chartapp.models import Temperature


# Create your views here.
def view_func(request):
    queryset = Temperature.objects.all()
    values = [[str(e.datetime.time()), int(e.amount)] for e in queryset]
    return render(request, 'template.html', {'values': values})
