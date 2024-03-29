from django.contrib import admin

# Register your models here.
from . models import Client, Address


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email_address')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ('street_name', 'city', 'zip_code', 'country')
    list_display = ('street_name', 'city', 'country')
    list_filter = ('street_name', 'city', 'country')
    ordering = ('street_name',)
