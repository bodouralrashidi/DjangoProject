from django.contrib import admin

from . models import Product,Offer


#offer section

class offerAdmin(admin.ModelAdmin):
    list_display = ("code","discount")
admin.site.register(Offer,offerAdmin)



# add product in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock")

admin.site.register(Product,ProductAdmin)