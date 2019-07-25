from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render, get_object_or_404
from .models import Band


# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to bands")

# example with template (normal Django approach)
def home(request):
    return HttpResponse("Welcome to the Bands app")

def band_info(request, band_name):
    band = get_object_or_404(Band, name=band_name)
    context = {
        'band': band,
    }
    return render(request, 'bands/band_info.html', context)

