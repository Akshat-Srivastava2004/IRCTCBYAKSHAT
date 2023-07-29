from django.contrib import admin
from .models import passengerdetail



# Register your models here.
admin.site.site_header="IRCTC ADMIN PANEL"
@admin.register(passengerdetail)
class passengerdetailAdmin(admin.ModelAdmin):
    list_display=("id","passengername","Destination","Trainnumber","Tickets","Phonenumber")
