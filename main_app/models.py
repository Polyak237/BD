from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models


class Adjustment(models.Model):
    scale_length = models.FloatField('Длина мензуры', max_length=5, blank=False)
    scale_height = models.FloatField('Высота струн', max_length=5, blank=False)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name='Привязанный сотрудник',
                                 related_name='bodies9', null=True, blank=True)

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return '№' + str(self.pk) + ' с параметрами ' + str(self.scale_length) + ', ' + str(self.scale_height)


class Body(models.Model):
    colour = models.CharField('Цвет', max_length=100, blank=False)
    tremolo_system = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Система тремоло / бридж',
                                       related_name='bodies', null=True)
    pickup_neck = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Нековый звукосниматель',
                                    related_name='bodies1', null=True, blank=True)
    pickup_mid = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Средний звукосниматель',
                                   related_name='bodies2', null=True, blank=True)
    pickup_bridge = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Бриджевый звукосниматель',
                                      related_name='bodies3', null=True, blank=True)
    form = models.CharField('Форма', max_length=50, blank=False)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Материал корпуса',
                                 related_name='bodies4', null=True)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name='Привязанный сотрудник',
                                 related_name='bodies5', null=True, blank=True)

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'

    def __str__(self):
        return '№' + str(self.pk) + ' цвета ' + str(self.colour) + ' формы ' + str(self.form)


class Client(models.Model):
    f = models.CharField('Фамилия', max_length=20, blank=False, null=True)
    i = models.CharField('Имя', max_length=20, blank=False, null=True)
    o = models.CharField('Отчество', max_length=20, blank=True, null=True, default='')
    card = models.CharField('Клубная карта', max_length=10, blank=False, null=True)
    passport = models.CharField('Паспорт', max_length=12, blank=False, null=True)
    phone_number = models.CharField('Номер телефона', max_length=16, blank=False)
    email = models.EmailField('Электронная почта', max_length=50, blank=True)
    kolvo_zakazov = models.IntegerField('Количество заказов', blank=True, null=True)
    priv_lvl = models.IntegerField('Уровень привилегий', blank=True, null=True)
    skidka = models.FloatField('Скидка', blank=True, null=True, default=0)

    def save(self, *args, **kwargs):
        if self.kolvo_zakazov < 3:
            self.priv_lvl = 1
        elif 3 <= self.kolvo_zakazov < 7:
            self.priv_lvl = 2
            self.skidka = 0.1
        elif self.kolvo_zakazov >= 7:
            self.priv_lvl = 3
            self.skidka = 0.2
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.f + ' ' + self.i


class Employee(models.Model):
    f = models.CharField('Фамилия', max_length=30, blank=False, null=True)
    i = models.CharField('Имя', max_length=30, blank=False, null=True)
    o = models.CharField('Отчество', max_length=30, blank=True, null=True, default='')
    passport = models.CharField('Паспорт', max_length=12, blank=False, null=True)
    phone_number = models.CharField('Номер телефона', max_length=16, blank=False)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, verbose_name='Должность',
                                 related_name='employees', null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.f + ' ' + self.i


class Fingerboard(models.Model):
    tuning_machine = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Колки',
                                       related_name='fin', null=True)
    pins = models.CharField('Метки на грифе', max_length=50, blank=False)
    headstock = models.FileField('Форма головы', upload_to='photo', blank=False)
    profile = models.CharField('Профиль', max_length=50, blank=True, null=True)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Материал накладки',
                                 related_name='fin1', null=True)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name='Привязанный сотрудник',
                                 related_name='fin1', null=True, blank=True)

    class Meta:
        verbose_name = 'Гриф'
        verbose_name_plural = 'Грифы'

    def __str__(self):
        return '№' + str(self.pk)


class Material(models.Model):
    name = models.CharField('Название', max_length=30, blank=False)
    amount_material = models.FloatField('Количество материала на складе (кг/шт.)', blank=False, null=True)

    TYPES = (
        ('Древесина для корпуса', 'Древесина для корпуса'),
        ('Древесина для грифа', 'Древесина для грифа'),
        ('Тремоло/бридж', 'Тремоло/бридж'),
        ('Звукосниматель', 'Звукосниматель'),
        ('Колки', 'Колки')
    )
    type = models.CharField('Тип компонента', choices=TYPES, max_length=50, default='Не выбран')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('Название', max_length=30, blank=False)
    salary = models.IntegerField('Зарплата', blank=False)
    duties = models.TextField('Обязанности', max_length=500, blank=False)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Provider(models.Model):
    title = models.CharField('Название', max_length=50, blank=False)
    office_address = models.CharField('Адрес офиса', max_length=70, blank=True, null=True)
    phone_number = models.CharField('Контактный телефон', max_length=16, blank=False)
    contact_name = models.CharField('ФИО контактного лица', max_length=70, blank=True, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name='Привязанный сотрудник',
                                 related_name='providers', null=True, blank=True)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title


class Supply(models.Model):
    nomer = models.IntegerField('id поставки', blank=False)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, verbose_name='Материал',
                                 related_name='materials', null=True)
    amount_material = models.FloatField('Количество материала (кг/шт.)', blank=False, null=True)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, verbose_name='Поставщик',
                                 related_name='supplies', null=True)
    date = models.DateTimeField('Дата и время поставки', blank=False)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name='Привязанный сотрудник',
                                 related_name='supplies', null=True, blank=True)

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

    def __str__(self):
        return '№' + str(self.nomer)


class Zakaz(models.Model):
    body = models.OneToOneField('Body', on_delete=models.SET_NULL, verbose_name='Корпус', related_name='zakaz',
                                blank=True, default='', null=True)
    fin = models.OneToOneField('Fingerboard', on_delete=models.SET_NULL, verbose_name='Гриф', related_name='zakaz',
                               blank=True, default='', null=True)
    adj = models.OneToOneField('Adjustment', on_delete=models.SET_NULL, verbose_name='Настройка', related_name='zakaz',
                               blank=True, default='', null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, verbose_name='Клиент', related_name='zakazbI',
                               blank=True, default='', null=True)
    requirements = models.TextField('Требования клиента', blank=False)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name='Привязанный сотрудник',
                                 related_name='zakazbI', null=True, blank=True)
    price = models.IntegerField('Предварительная цена', blank=False, default=0, null=True)

    itog_Price = models.FloatField('Сумма к оплате', blank=True, default=0, null=True)

    def save(self, *args, **kwargs):
        if self.client:
            self.itog_Price = self.price * (1 - self.client.skidka)
        else:
            self.itog_Price = self.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '№' + str(self.pk)

# class Pet(models.Model):
#     TYPES = (('Кошка', 'Кошка'),
#              ('Собака', 'Собака'))
#     name = models.CharField('Кличка', max_length=50, blank=False)
#     type = models.CharField('Вид', choices=TYPES, max_length=30, default='Кошка')
#     weight = models.FloatField('Вес', null=False)
#     breed = models.CharField('Порода', max_length=50, blank=False)
#     recommendations = models.TextField('Рекомендации', max_length=1000, blank=True)
#
#     client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент',
#                                related_name='pets')
#
#     class Meta:
#         verbose_name = 'Питомец'
#         verbose_name_plural = 'Питомцы'
#
#     def __str__(self):
#         return self.name
#
#
# class Request(models.Model):
#     description = models.TextField('Описание', max_length=200, blank=False)
#     pet = models.ForeignKey('Pet', on_delete=models.SET_NULL, verbose_name='Питомец',
#                             related_name='requests', null=True)
#
#     class Meta:
#         verbose_name = 'Заявка'
#         verbose_name_plural = 'Заявки'
#
#     def __str__(self):
#         return 'Заявка №' + str(self.id)
#
#
# class Order(models.Model):
#     STATUSES = (
#         ('Создан', 'Создан'),
#         ('Ожидает подписания договора', 'Ожидает подписания договора'),
#         ('Ожидает оплаты', 'Ожидает оплаты'),
#         ('В транспортировке (от владельца)', 'В транспортировке (от владельца)'),
#         ('На передержке', 'На передержке'),
#         ('В транспортировке (к владельцу)', 'В транспортировке (к владельцу)'),
#         ('Завершен', 'Завершен'),
#         ('Отменен', 'Отменен')
#     )
#     status = models.CharField('Статус', choices=STATUSES, max_length=40, default='Создан')
#     request = models.OneToOneField('Request', on_delete=models.SET_NULL, verbose_name='Заявка',
#                                    related_name='order', null=True)
#     workers = models.ManyToManyField('Worker', verbose_name='Работники',
#                                      related_name='orders', blank=True)
#
#     def clean(self):
#         if self.duration <= 0:
#             raise ValidationError('Длительность не может быть менее 1 дня')
#
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#     def __str__(self):
#         return 'Заказ №' + str(self.id)
#
#
# class Agreement(models.Model):
#     description = models.TextField('Описание', max_length=200, blank=False)
#     price = models.IntegerField('Стоимость, руб.')
#     order = models.OneToOneField('Order', on_delete=models.SET_NULL, verbose_name='Заказ',
#                                  related_name='agreement', null=True)
#
#     def clean(self):
#         if self.price <= 0:
#             raise ValidationError('Стоимость не может быть менее 1 руб.')
#
#     class Meta:
#         verbose_name = 'Договор'
#         verbose_name_plural = 'Договоры'
#
#     def __str__(self):
#         return 'Договор №' + str(self.id)
#
#
# class Worker(models.Model):
#     POSITIONS = (
#         ('Перевозчик', 'Перевозчик'),
#         ('Кипер', 'Кипер')
#     )
#     first_name = models.CharField('Имя', max_length=50, blank=False)
#     last_name = models.CharField('Фамилия', max_length=50, blank=False)
#     middle_name = models.CharField('Отчетство', max_length=50, blank=True)
#     phone_number = models.CharField('Номер телефона', max_length=20, blank=False)
#     email = models.EmailField('Email', blank=True)
#     position = models.CharField('Должность', choices=POSITIONS, max_length=40, default='Кипер')
#
#     class Meta:
#         verbose_name = 'Работник'
#         verbose_name_plural = 'Работники'
#
#     def __str__(self):
#         return self.position + ' | ' + self.last_name + ' ' + self.first_name
#
#
# class Car(models.Model):
#     POSITIONS = (
#         ('Перевозчик', 'Перевозчик'),
#         ('Кипер', 'Кипер')
#     )
#     numbers = models.CharField('Номера', max_length=50)
#     mark_n_model = models.CharField('Марка, модель', max_length=50)
#     color = models.CharField('Цвет', max_length=50, blank=True)
#     worker = models.ForeignKey('Worker', on_delete=models.SET_NULL, verbose_name='Работник',
#                                related_name='cars', null=True)
#
#     class Meta:
#         verbose_name = 'Машина'
#         verbose_name_plural = 'Машины'
#
#     def __str__(self):
#         return self.mark_n_model + ' ' + self.numbers
#
#
# class TransportEvent(models.Model):
#     timestamp_start = models.DateTimeField('Время начала', default=timezone.now)
#     timestamp_end = models.DateTimeField('Время конца', default=timezone.now)
#     description = models.TextField('Описание', max_length=200, blank=False)
#     order = models.ForeignKey('Order', on_delete=models.SET_NULL, verbose_name='Заказ',
#                               related_name='transport_events', null=True)
#
#     class Meta:
#         verbose_name = 'Событие перевозки'
#         verbose_name_plural = 'События перевозки'
#
#     def __str__(self):
#         return 'Перевозка №' + str(self.id)
#
#
# class Report(models.Model):
#     created_at = models.DateTimeField('Время создания', default=timezone.now)
#     description = models.TextField('Описание', max_length=200, blank=False)
#     order = models.ForeignKey('Order', on_delete=models.SET_NULL, verbose_name='Заказ',
#                               related_name='reports', null=True)
#     video = models.FileField('Видеофайл', upload_to='report_videos')
#     image = models.ImageField('Изображение', upload_to='report_images')
#
#     def clean(self):
#         approved_video_extensions = ('.mp4', '.ogv', '.webm', 'webvtt')
#         if not self.video.name.lower().endswith(approved_video_extensions):
#             raise ValidationError(
#                 f"Расширение видеофайла может быть только одим из следующих: {', '.join(approved_video_extensions)}")
#
#     class Meta:
#         verbose_name = 'Отчет'
#         verbose_name_plural = 'Отчеты'
#
#     def __str__(self):
#         return 'Отчет №' + str(self.id)
