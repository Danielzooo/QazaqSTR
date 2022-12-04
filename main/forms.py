from django import forms
from .const.choise import FactorynameChoise
from .models import SaveConcreate


class CreateConcreteForms(forms.Form):
    model = SaveConcreate
    data = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'class': 'form-control'}))
    factory_name = forms.ChoiceField(label='Завод', choices=FactorynameChoise
                                     , widget=forms.TextInput(attrs={'class': 'form-control'}))
    object_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название объекта'}),
    block = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mark = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Марка бетона'}),
    constructive = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Конструктив'}),
    floor = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Этаж'}),
    fact_concrete = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Факт'}),
    sum_concrete = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Итого залито'}),
    accepted = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кто принимал'}),

