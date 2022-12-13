from django.contrib import admin
from .models import User,Routes,UserProfile,Businesscard,Vehicalmodel,Attachnewlorry,phoneModel

# Register your models here.
admin.site.register(User)
admin.site.register(Routes)
admin.site.register(UserProfile)

class Businesscardadmin(admin.ModelAdmin):
    list_display =  ['contact_person_name','Designation','Alternative_contact','Email','Logo','Bussiness_Address']
admin.site.register(Businesscard,Businesscardadmin)


class Vehicalmodeladmin(admin.ModelAdmin):
    list_display =  ['Vehicle_name','Vehicle_load_capacity','Vehicle_Type','Is_Tyres_defined']
admin.site.register(Vehicalmodel,Vehicalmodeladmin)



class Attachnewlorryadmin(admin.ModelAdmin):
    list_display =  ['UserVehicle_number','Current_location','Permit','Is_all_permit','Vehicle','Is_active','Is_Rc_verfied']
admin.site.register(Attachnewlorry,Attachnewlorryadmin)


admin.site.register(phoneModel)

