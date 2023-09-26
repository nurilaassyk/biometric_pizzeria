from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from api_pizzeria.selectors import pizzeria_list


class PizzeriaListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        address = serializers.CharField()

    def get(self, request):
        pizzerias = pizzeria_list()
        data = self.OutputSerializer(pizzerias, many=True).data
        return Response(data)


