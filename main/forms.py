from django import forms
from .const.choise import FactorynameChoise, MarkChoise, ConstructiveChoise
from .models import SaveConcreate


class CreateConcreteForms(forms.Form):
    model = SaveConcreate
    data = forms.DateField(label='Дата')
    factory_name = forms.ChoiceField(label='Завод', choices=FactorynameChoise.choices)
    object_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название объекта'}),
    block = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mark = forms.ChoiceField(label='Завод', choices=MarkChoise.choices),
    constructive = forms.ChoiceField(label='Завод', choices=ConstructiveChoise.choices),
    floor = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Этаж'}),
    fact_concrete = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Факт'}),
    sum_concrete = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Итого залито'}),
    accepted = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кто принимал'}),

