from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from apps.client.api.serializers.client_serializers import ClientSerializer, ClientListSerializer
from apps.client.models import Client

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    List_serializer_class = ClientListSerializer
    #parser_class = (FileUploadParser,)
    
    def get_queryset(self):
        return Client.objects.all()
    
    def list(self, request):
        client_serialize =  self.List_serializer_class(self.get_queryset(), many = True)
        return Response(client_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empleado Correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        client =  Client.objects.filter(idclient = pk).first()
        if client:
            client_serializer = self.serializer_class(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        client =  Client.objects.filter(idclient = pk).first()
        if client:
            if client:
                client_serializer = self.serializer_class(client,data = request.data)
                if client_serializer.is_valid():
                    client_serializer.save()
                    return Response({'message':'Empleado Correctamente'}, status=status.HTTP_200_OK)
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        client = Client.objects.filter(idclient = pk).first()
        if client:
            self.perform_destroy(self.get_object())
            return Response({'message':'Empleado Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST) 