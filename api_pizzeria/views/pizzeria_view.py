from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from api_pizzeria.selectors import pizzeria_list, pizzeria_detail
from api_pizzeria.services import create_pizzeria, pizzeria_update, pizzeria_delete


class PizzeriaListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        address = serializers.CharField()

    class Meta:
        ref_name = 'PizzeriaListOutputSerializer'

    def get(self, request):
        pizzerias = pizzeria_list()
        data = self.OutputSerializer(pizzerias, many=True).data
        return Response(data)


class PizzeriaCreateApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        address = serializers.CharField()

        class Meta:
            ref_name = 'PizzeriaCreateOutputSerializer'

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        address = serializers.CharField()

        class Meta:
            ref_name = 'PizzeriaCreateInputSerializer'

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pizzeria = create_pizzeria(**serializer.validated_data)
        pizzeria = pizzeria_detail(pizzeria.pk)
        data = self.OutputSerializer(pizzeria).data
        return Response(data)


class PizzeriaDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        address = serializers.CharField()

        class Meta:
            ref_name = 'PizzeriaDetailOutputSerializer'

    def get(self, request, pk):
        pizzeria = pizzeria_detail(pk)
        data = self.OutputSerializer(pizzeria).data
        return Response(data)


class PizzeriaUpdateApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        address = serializers.CharField()

        class Meta:
            ref_name = 'PizzeriaUpdateOutputSerializer'

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        address = serializers.CharField()

        class Meta:
            ref_name = 'PizzeriaUpdateInputSerializer'

    def post(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.data.get('name')
        address = serializer.data.get('address')
        pizzeria = pizzeria_update(name, address, pk)
        pizzeria = pizzeria_detail(pizzeria.pk)
        data = self.OutputSerializer(pizzeria).data
        return Response(data)


class PizzeriaDeleteApi(APIView):

    def post(self, request, pk):
        pizzeria_delete(pk)
        data = {"detail": "Pizzeria deleted successfully"}
        return Response(data)
