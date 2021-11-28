from django.contrib.admin import AdminSite
from django.contrib import admin

from .models import *

AdminSite.index_title = 'Администрация сайта'
AdminSite.site_title = 'Магазин музыкальных инструментов на заказ "MusicTecH"'
AdminSite.site_header = 'Магазин музыкальных инструментов на заказ "MusicTecH"'


class Adjustment1(admin.ModelAdmin):
    list_display = ('pk', 'Scale_length', 'Scale_height', 'id_employee')


class Body1(admin.ModelAdmin):
    list_display = ('pk', 'Colour', 'Form', 'Material')


class Client1(admin.ModelAdmin):
    list_display = ('F', 'I', 'O', 'Card', 'Phone_number', 'Kolvo_zakazov', 'Priv_lvl')

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     self.exclude = ('Skidka', )
    #     return qs

class Employee1(admin.ModelAdmin):
    list_display = ('FIO', 'Phone_number', 'Position')


class Fingerboard1(admin.ModelAdmin):
    list_display = ('pk', 'Material', 'Tuning_machine', 'Headstock')


class Material1(admin.ModelAdmin):
    list_display = ('Name', 'Amount_material')


class Position1(admin.ModelAdmin):
    list_display = ('Name', 'Salary', 'Duties')


class Provider1(admin.ModelAdmin):
    list_display = ('Title', 'Office_address', 'Phone_number', 'Contact_name')


class Supply1(admin.ModelAdmin):
    list_display = ('Nomer', 'Material', 'Provider', 'Date', 'Employee')


class Zakaz1(admin.ModelAdmin):
    list_display = ('pk', 'Client', 'Body', 'Fingerboard', 'Adjustment', 'Itog_Price')


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
# class AgreementAdmin(admin.ModelAdmin):
#     list_display = ('order', 'description', 'price')
#
#
# class WorkerAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'position')
#
#
# class CarAdmin(admin.ModelAdmin):
#     list_display = ('numbers', 'mark_n_model', 'color', 'worker')
#
#
# class TransportEventAdmin(admin.ModelAdmin):
#     list_display = ('order', 'timestamp_start', 'timestamp_end', 'description')
#
#
# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('order', 'created_at', 'description', 'video', 'image')
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
