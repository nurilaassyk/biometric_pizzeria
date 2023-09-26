from api_pizzeria.models import PizzeriaModel


def pizzeria_list():
    return PizzeriaModel.objects.all()

