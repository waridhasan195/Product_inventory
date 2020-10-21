from django.contrib import admin
from .models import *
from .forms import ComputerForm

@admin.register(Computer)
class Computer_admin_view(admin.ModelAdmin):
    list_display = ['computer_name', 'operating_system', 'IP_address', 'MAC_address', 'user_name', 'location', 'purchase_date', 'timestamp']
    form = ComputerForm
    list_filter = ['computer_name', 'IP_address', 'location']
    search_fields = ['computer_name', 'IP_address', 'location']

admin.site.register(Operating_system)