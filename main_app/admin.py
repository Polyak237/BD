from django.contrib.admin import AdminSite
from django.contrib import admin

from .models import *

AdminSite.index_title = 'Администрация сайта'
AdminSite.site_title = 'Магазин музыкальных инструментов на заказ "MusicTecH"'
AdminSite.site_header = 'Магазин музыкальных инструментов на заказ "MusicTecH"'


class Adjustment1(admin.ModelAdmin):
    list_display = ('pk', 'scale_length', 'scale_height', 'id_employee')


class Body1(admin.ModelAdmin):
    list_display = ('pk', 'colour', 'form', 'material')


class Client1(admin.ModelAdmin):
    list_display = ('f', 'i', 'o', 'card', 'phone_number', 'kolvo_zakazov', 'priv_lvl')

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     self.exclude = ('skidka', )
    #     return qs

class Employee1(admin.ModelAdmin):
    list_display = ('f', 'i', 'o', 'phone_number', 'position')


class Fingerboard1(admin.ModelAdmin):
    list_display = ('pk', 'material', 'tuning_machine', 'headstock')


class Material1(admin.ModelAdmin):
    list_display = ('name', 'amount_material')


class Position1(admin.ModelAdmin):
    list_display = ('name', 'salary', 'duties')


class Provider1(admin.ModelAdmin):
    list_display = ('title', 'office_address', 'phone_number', 'contact_name')


class Supply1(admin.ModelAdmin):
    list_display = ('nomer', 'material', 'provider', 'date', 'employee')


class Zakaz1(admin.ModelAdmin):
    list_display = ('pk', 'client', 'body', 'fingerboard', 'adjustment', 'itog_Price')


#     list_display = ('pet', 'description')
#     list_filter = ('pet',)
#     search_fields = ('description',)
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('request', 'created_at', 'duration', 'status')
#     list_filter = ('created_at', 'status')
#     search_fields = ('duration', 'status')
#
#

admin.site.register(Adjustment, Adjustment1)
admin.site.register(Body, Body1)
admin.site.register(Client, Client1)
admin.site.register(Employee, Employee1)
admin.site.register(Fingerboard, Fingerboard1)
admin.site.register(Material, Material1)
admin.site.register(Position, Position1)
admin.site.register(Provider, Provider1)
admin.site.register(Supply, Supply1)
admin.site.register(Zakaz, Zakaz1)
