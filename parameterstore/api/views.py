from symbol import parameters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .searializers import ParameterSerializer
from .models import Parameter
from .helper import Encryption

class ParameterViewSet(ViewSet, GenericAPIView):
    """
    ViewSet to perform CRUD on Parameter
    """

    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
    cipher_suite = Encryption

    def list(self, request):
        data = self.queryset

        for param in data:
            if param.flag:
                param.value = self.cipher_suite.decrypt(bytes(param.value, 'utf-8'))

        serializer = ParameterSerializer(data, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        if data.get('flag'):
            data['value'] = self.cipher_suite.encrypt(data.get('value')).decode()

        serializer = ParameterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        parameter = get_object_or_404(self.queryset, pk=pk)

        if parameter.flag:
            parameter.value = self.cipher_suite.decrypt(bytes(parameter.value, 'utf-8'))

        serializer = ParameterSerializer(parameter)
        return Response(serializer.data)

    def update(self, request, pk=None):
        parameter = get_object_or_404(self.queryset, pk=pk)
        data = request.data

        if data.get('flag'):
            data['value'] = self.cipher_suite.encrypt(data['value']).decode()

        serializer = ParameterSerializer(parameter, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        parameter = get_object_or_404(self.queryset, pk=pk)
        data = request.data

        if data.get('flag') and data.get('value'):
            data['value'] = self.cipher_suite.encrypt(data['value']).decode()
        elif parameter.flag != data.get('flag') and data.get('flag') and not data.get('value'):
            parameter.value = self.cipher_suite.encrypt(parameter.value).decode()
        elif parameter.flag != data.get('flag') and not data.get('flag') and not data.get('value'):
            parameter.value = self.cipher_suite.decrypt(bytes(parameter.value, 'utf-8'))

        serializer = ParameterSerializer(parameter, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        parameter = get_object_or_404(self.queryset, pk=pk)
        serializer = ParameterSerializer(parameter)

        if parameter:
            parameter.delete()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
