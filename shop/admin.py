from django.contrib import admin
from .models import *

class PropertyAdmin(admin.ModelAdmin):
    list_display=('addrerss','property_image')
admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(PropertyFeature)
admin.site.register(ContractStatus)
admin.site.register(Contract)
admin.site.register(Offer)
admin.site.register(Client)
admin.site.register(Inspection)
admin.site.register(PropertyEmployee)
admin.site.register(RoleType)
admin.site.register(Employee)
admin.site.register(Listing)
admin.site.register(Feature)
admin.site.register(ListingType)




# Register your models here.
