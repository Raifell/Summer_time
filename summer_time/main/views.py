from django.shortcuts import render
from .models import IcecreamSale, IcecreamShop, Icecream, Kid, KidParent


def main_page(request):
    data = None
    variable = None
    if request.method == 'GET':
        if 'kids' in request.GET:
            data = Kid.objects.all()
            variable = 'kids'
        elif 'parents' in request.GET:
            data = KidParent.objects.all()
            variable = 'parents'
        elif 'icecreams' in request.GET:
            data = Icecream.objects.all()
            variable = 'icecreams'
        elif 'shops' in request.GET:
            data = IcecreamShop.objects.all()
            variable = 'shops'
        elif 'sales' in request.GET:
            data = IcecreamSale.objects.all()
            variable = 'sales'

    return render(request, 'main/index_main.html', {'data': data, 'variable': variable})


def info_page(request, info_slug):
    data = None
    anchor = None
    for find in [Kid, KidParent, Icecream, IcecreamShop, IcecreamSale]:
        if not data:
            anchor = find._meta.db_table
            data = find.objects.filter(slug=info_slug)
    # print('\n', data, anchor, '\n')
    return render(request, 'main/index_info.html', {'data': data[0], 'anchor': anchor})
