from rest_framework.response import Response

from api_pizzeria.models import PizzeriaModel, PizzaModel


def create_pizzeria(name: str, address: str):
    pizzeria = PizzeriaModel(name=name, address=address)
    pizzeria.save()
    return pizzeria


def pizzeria_update(name: str, address: str, pk: int):
    pizzeria = PizzeriaModel.objects.get(pk=pk)
    pizzeria.name = name
    pizzeria.address = address
    pizzeria.save()
    return pizzeria


def pizzeria_delete(pk):
    pizzeria = PizzeriaModel.objects.get(pk=pk)
    pizzeria.deleted_at = True
    pizzeria.save()
    return None


def pizza_create(name: str, cheese: str, dough: str, secret_ingredient: str):
    pizza = PizzaModel(name=name, cheese=cheese, dough=dough, secret_ingredient=secret_ingredient)
    pizza.save()
    return pizza


def pizza_update(name: str, cheese: str, dough: str, secret_ingredient: str, pk: int):
    pizza = PizzaModel.objects.get(pk=pk)
    pizza.name = name
    pizza.cheese = cheese
    pizza.dough = dough
    pizza.secret_ingredient = secret_ingredient
    pizza.save()
    return pizza


def pizza_delete(pk):
    pizza = PizzaModel.objects.get(pk=pk)
    pizza.deleted_at = True
    pizza.save()
    return None
