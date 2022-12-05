from django.db import models
from main.const.choise import FactorynameChoise, ConstructiveChoise, MarkChoise
from main.const import AbstractTimeTracker


class Registration(AbstractTimeTracker):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    phone = models.IntegerField('Телефон номер', unique=True)
    sms = models.IntegerField('введите СМС')


class SaveConcreate(AbstractTimeTracker):
    data = models.DateField('Дата заполнение', max_length=20)
    factory_name = models.CharField(choices=FactorynameChoise.choices,
                                    max_length=255,
                                    verbose_name=('Название завода')
                                    )
    object_name = models.CharField('Название объекта', max_length=50)
    block = models.IntegerField('блок')
    mark = models.CharField(choices=MarkChoise.choices,max_length=255, verbose_name=('Марка'))
    constructive = models.CharField(choices=ConstructiveChoise.choices,
                                    max_length=255,
                                    verbose_name=('Конструктив')
                                    )
    floor = models.IntegerField('Этаж')
    fact_concrete = models.IntegerField('Факт')
    sum_concrete = models.IntegerField('Итого залито')
    accepted = models.ForeignKey('Registration', on_delete=models.CASCADE)

    def __int__(self):
        return self.data

    class Meta:
        verbose_name = 'Таблица бетона'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return f'/{self.id}'


