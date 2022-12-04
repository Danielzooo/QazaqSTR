from django.shortcuts import render, redirect
from ..models import SaveConcreate
from ..forms import CreateConcreteForms
from django.views.generic import UpdateView, DeleteView, DetailView


def base(request):
    return render(request, 'base.html')


def table(request):
    model_concrete = SaveConcreate.objects.all()
    return render(request, 'table.html', {'model_concrete': model_concrete})


def create(request):
    context = {}
    context['form'] = CreateConcreteForms()
    if request.method == 'POST':
        form = CreateConcreteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')
        else:
            error = 'Не правильно заполнили'

    return render(request, 'create.html', context)


class ConcreteDetailView(DetailView):
    model = SaveConcreate
    template_name = 'detail.html'
    context_object_name = 'el'


class ConcreteUpdateView(UpdateView):
    model = SaveConcreate
    template_name = 'create.html'
    form_class = CreateConcreteForms


class ConcreteDeleteView(DeleteView):
    model = SaveConcreate
    success_url = 'http://127.0.0.1:8000/table'
    template_name = 'delete.html'

