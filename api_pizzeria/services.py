from django.shortcuts import get_object_or_404

from api_pizzeria.models import PizzeriaModel, PizzaModel


def create_pizzeria(name: str, address: str):
    pizzeria = PizzeriaModel(name=name, address=address)
    pizzeria.save()
    return pizzeria


def pizzeria_update(pk, **kwargs):
    pizzeria = get_object_or_404(PizzeriaModel, pk=pk)
    PizzeriaModel.objects.filter(pk=pk).update(**kwargs)
    pizzeria.refresh_from_db()
    return pizzeria


def pizzeria_delete(pk):
    pizzeria = get_object_or_404(PizzeriaModel, pk=pk)
    pizzeria.deleted_at = True
    pizzeria.save()
    return None


def pizza_create(pizzeria: PizzeriaModel, name: str, cheese: str, dough: str, secret_ingredient: str):
    pizza = PizzaModel(pizzeria=pizzeria, name=name, cheese=cheese, dough=dough,
                       secret_ingredient=secret_ingredient)
    pizza.save()
    return pizza


def pizza_update(pk, **kwargs):
    pizza = get_object_or_404(PizzaModel, pk=pk)
    PizzaModel.objects.filter(pk=pk).update(**kwargs)
    pizza.refresh_from_db()
    return pizza


def pizza_delete(pk):
    pizza = get_object_or_404(PizzaModel, pk=pk)
    pizza.deleted_at = True
    pizza.save()
    return None
