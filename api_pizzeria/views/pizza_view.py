from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from api_pizzeria.selectors import pizza_list, pizza_detail
from api_pizzeria.services import pizza_create, pizza_delete, pizza_update


class PizzaListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaListOutputSerializer'

    def get(self, request):
        pizza = pizza_list()
        data = self.OutputSerializer(pizza, many=True).data
        return Response(data)


class PizzaCreateApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaCreateOutputSerializer'

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaCreateInputSerializer'

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pizza = pizza_create(**serializer.validated_data)
        pizza = pizza_detail(pizza.pk)
        data = self.OutputSerializer(pizza).data
        return Response(data)


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
        return Response(data)


class PizzaUpdateApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaUpdateOutputSerializer'

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        cheese = serializers.CharField()
        dough = serializers.CharField()
        secret_ingredient = serializers.CharField()

        class Meta:
            ref_name = 'PizzaUpdateInputSerializer'

    def post(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.data.get('name')
        cheese = serializer.data.get('cheese')
        dough = serializer.data.get('dough')
        secret_ingredient = serializer.data.get('secret_ingredient')

        pizza = pizza_update(name, cheese, dough, secret_ingredient, pk)
        pizza = pizza_detail(pizza.pk)
        data = self.OutputSerializer(pizza).data
        return Response(data)


class PizzaDeleteApi(APIView):
    def post(self, request, pk):
        pizza_delete(pk)
        data = {"detail": "Pizza deleted successfully"}
        return Response(data)
