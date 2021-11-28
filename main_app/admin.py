from django.contrib.admin import AdminSite
from django.contrib import admin

from .models import *

AdminSite.index_title = 'Администрация сайта'
AdminSite.site_title = 'Магазин музыкальных инструментов на заказ "MusicTecH"'
AdminSite.site_header = 'Магазин музыкальных инструментов на заказ "MusicTecH"'


class Adjustment1(admin.ModelAdmin):
    list_display = ('pk', 'scale_length', 'scale_height', 'employee')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(position__name='Настройщик')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Body1(admin.ModelAdmin):
    list_display = ('pk', 'colour', 'form', 'material')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(position__name='Сборщик')
        elif db_field.name == "tremolo_system":
            kwargs["queryset"] = Material.objects.filter(type='Тремоло/бридж')
        elif db_field.name == "pickup_neck":
            kwargs["queryset"] = Material.objects.filter(type='Звукосниматель')
        elif db_field.name == "pickup_mid":
            kwargs["queryset"] = Material.objects.filter(type='Звукосниматель')
        elif db_field.name == "pickup_bridge":
            kwargs["queryset"] = Material.objects.filter(type='Звукосниматель')
        elif db_field.name == "material":
            kwargs["queryset"] = Material.objects.filter(type='Древесина для корпуса')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Client1(admin.ModelAdmin):
    list_display = ('f', 'i', 'o', 'card', 'phone_number', 'kolvo_zakazov', 'priv_lvl')
    readonly_fields = ('priv_lvl', 'skidka')
    search_fields = ('card', 'f',)
    list_filter = ('priv_lvl',)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     self.exclude = ('skidka', )
    #     return qs


class Employee1(admin.ModelAdmin):
    list_display = ('f', 'i', 'o', 'phone_number', 'position')
    list_filter = ('position',)


class Fingerboard1(admin.ModelAdmin):
    list_display = ('pk', 'material', 'tuning_machine', 'headstock')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(position__name='Сборщик')
        elif db_field.name == "tuning_machine":
            kwargs["queryset"] = Material.objects.filter(type='Колки')
        elif db_field.name == "material":
            kwargs["queryset"] = Material.objects.filter(type='Древесина для грифа')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Material1(admin.ModelAdmin):
    list_display = ('name', 'amount_material', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

class Position1(admin.ModelAdmin):
    list_display = ('name', 'salary', 'duties')


class Provider1(admin.ModelAdmin):
    list_display = ('title', 'office_address', 'phone_number', 'contact_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(position__name='Менеджер')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Supply1(admin.ModelAdmin):
    list_display = ('nomer', 'material', 'provider', 'date', 'employee')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(position__name='Менеджер')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Zakaz1(admin.ModelAdmin):
    list_display = ('pk', 'client', 'body', 'fin', 'adj', 'employee', 'itog_Price')
    readonly_fields = ('itog_Price',)
    list_filter = ('client', 'employee',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(position__name='Менеджер')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     self.exclude = ('skidka', )
    #     return qs


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
