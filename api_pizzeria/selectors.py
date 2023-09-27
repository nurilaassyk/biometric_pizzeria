from django.shortcuts import get_object_or_404

from api_pizzeria.models import PizzeriaModel, PizzaModel


def pizzeria_list():
    return PizzeriaModel.objects.filter(is_deleted=False)


def pizzeria_detail(pk):
    pizzeria = get_object_or_404(PizzeriaModel, pk=pk)
    return pizzeria


def pizza_list():
    return PizzaModel.objects.filter(is_deleted=False)


def pizza_detail(pk):
    pizza = get_object_or_404(PizzaModel, pk=pk)
    return pizza


def pizzeria_pizza_list(pk):
    pizzeria = get_object_or_404(PizzeriaModel, pk=pk)
    pizza = pizzeria.pizza.filter(is_deleted=False)
    return pizza
