from api_pizzeria.models import PizzeriaModel, PizzaModel


def pizzeria_list():
    return PizzeriaModel.objects.filter(deleted_at=False)


def pizzeria_detail(pk):
    pizzeria = PizzeriaModel.objects.get(pk=pk)
    return pizzeria


def pizza_list():
    return PizzaModel.objects.filter(deleted_at=False)


def pizza_detail(pk):
    pizza = PizzaModel.objects.get(pk=pk)
    return pizza
