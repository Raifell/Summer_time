from django.contrib import admin
from .models import KidParent, Kid, Icecream, IcecreamShop, IcecreamSale

admin.site.register(Kid)
admin.site.register(KidParent)
admin.site.register(Icecream)
admin.site.register(IcecreamShop)
admin.site.register(IcecreamSale)
