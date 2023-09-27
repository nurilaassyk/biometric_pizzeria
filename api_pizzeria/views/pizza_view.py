from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from api_pizzeria.selectors import pizza_list, pizza_detail, pizzeria_detail
from api_pizzeria.services import pizza_create, pizza_delete, pizza_update


class PizzaListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        pizzeria = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaListOutputSerializer'

    def get(self, request):
        pizza = pizza_list()
        data = self.OutputSerializer(pizza, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PizzaCreateApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        pizzeria = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaCreateOutputSerializer'

    class InputSerializer(serializers.Serializer):
        pizzeria_id = serializers.IntegerField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaCreateInputSerializer'

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        pizzeria = pizzeria_detail(validated_data.pop('pizzeria_id'))
        pizza = pizza_create(pizzeria=pizzeria, **serializer.validated_data)
        data = self.OutputSerializer(pizza).data
        return Response(data, status=status.HTTP_201_CREATED)


class PizzaDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaDetailOutputSerializer'

    def get(self, request, pk):
        pizza = pizza_detail(pk)
        data = self.OutputSerializer(pizza).data
        return Response(data, status=status.HTTP_200_OK)


class PizzaUpdateApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        pizzeria = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaUpdateOutputSerializer'

    class InputSerializer(serializers.Serializer):
        pizzeria_id = serializers.IntegerField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaUpdateInputSerializer'

    def post(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pizza = pizza_update(pk, **serializer.data)
        data = self.OutputSerializer(pizza).data
        return Response(data, status=status.HTTP_200_OK)


class PizzaDeleteApi(APIView):
    def post(self, request, pk):
        pizza_delete(pk)
        data = {"detail": "Pizza deleted successfully"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
