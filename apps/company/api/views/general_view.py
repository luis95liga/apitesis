from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from apps.company.utils import validate_files
from apps.company.models import (
    Country,
    Locality,
    Province,
    DocumentType,
    Documents
)
from apps.company.api.serializers.general_serializes import (
    CountrySerializer,
    LocalitySerializer,
    LocalityListSerializer,
    ProvinceSerializer,
    ProvinceListSerializer,
    DocumentTypeSerializer,
    DocumentsSerializer,
    DocumentsListSerializer
)

from rest_framework.response import Response

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer


    def get_queryset(self):
        return Country.objects.all()

    def list(self, request):
        country_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(country_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Pais creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        country =  Country.objects.filter(idcountry = pk).first()
        if country:
            country_serializer = self.serializer_class(country)
            return Response(country_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        country =  Country.objects.filter(idcountry = pk).first()
        if country:
            if country:
                country_serializer = self.serializer_class(country,data = request.data)
                if country_serializer.is_valid():
                    country_serializer.save()
                    return Response({'message':'Pais Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        country =  Country.objects.filter(idcountry = pk).first()
        if country:
            self.perform_destroy(self.get_object())
            return Response({'message':'Pais Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class LocalityViewSet(viewsets.ModelViewSet):
    serializer_class = LocalitySerializer
    list_serializer_class = LocalityListSerializer

    def get_queryset(self):
        return Locality.objects.all()

    def list(self, request):
        locality_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(locality_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'localidad creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        locality =  Locality.objects.filter(idlocation = pk).first()
        if locality:
            locality_serializer = self.serializer_class(locality)
            return Response(locality_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        locality =  Locality.objects.filter(idlocation = pk).first()
        if locality:
            if locality:
                locality_serializer = self.serializer_class(locality,data = request.data)
                if locality_serializer.is_valid():
                    locality_serializer.save()
                    return Response({'message':'Localidad Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(locality_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        locality =  Locality.objects.filter(idlocation = pk).first()
        if locality:
            self.perform_destroy(self.get_object())
            return Response({'message':'Localidad Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class ProvinceViewSet(viewsets.ModelViewSet):
    serializer_class = ProvinceSerializer
    list_serializer_class = ProvinceListSerializer

    def get_queryset(self):
        return Province.objects.all()

    def list(self, request):
        province_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(province_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Provincia creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        province =  Province.objects.filter(idprovince = pk).first()
        if province:
            province_serializer = self.serializer_class(province)
            return Response(province_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        province =  Province.objects.filter(idprovince = pk).first()
        if province:
            if province:
                province_serializer = self.serializer_class(province,data = request.data)
                if province_serializer.is_valid():
                    province_serializer.save()
                    return Response({'message':'Provincia Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(province_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        province =  Province.objects.filter(idprovince = pk).first()
        if province:
            self.perform_destroy(self.get_object())
            return Response({'message':'Provincia Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class DocumentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentTypeSerializer

    def get_queryset(self):
        return DocumentType.objects.all()

    def list(self, request):
        documenttype_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(documenttype_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de Documento creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        documenttype =  DocumentType.objects.filter(iddocument_type = pk).first()
        if documenttype:
            documenttype_serializer = self.serializer_class(documenttype)
            return Response(documenttype_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        documenttype =  DocumentType.objects.filter(iddocument_type = pk).first()
        if documenttype:
            if documenttype:
                documenttype_serializer = self.serializer_class(documenttype,data = request.data)
                if documenttype_serializer.is_valid():
                    documenttype_serializer.save()
                    return Response({'message':'Tipo de Documento Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(documenttype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        documenttype =  DocumentType.objects.filter(iddocument_type = pk).first()
        if documenttype:
            self.perform_destroy(self.get_object())
            return Response({'message':'Tipo de Documento Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializer
    list_serializer_class = DocumentsListSerializer

    def get_queryset(self):
        return Documents.objects.all()

    def list(self, request):
        documents_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(documents_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Documento creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        documents =  Documents.objects.filter(iddocument = pk).first()
        if documents:
            documents_serializer = self.serializer_class(documents)
            return Response(documents_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        data = validate_files(request.data,'attachment', True)
        print(data)
        documents =  Documents.objects.filter(iddocument = pk).first()
        if documents:
            if documents:
                documents_serializer = self.serializer_class(documents,data = request.data)
                if documents_serializer.is_valid():
                    documents_serializer.save()
                    print(documents_serializer.data)
                    return Response({'message':'Documento Actualizada Correctamente'}, status=status.HTTP_200_OK)
            print(documents_serializer.errors)
            return Response(documents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        documents =  Documents.objects.filter(iddocument = pk).first()
        if documents:
            self.perform_destroy(self.get_object())
            return Response({'message':'Documento Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class DocumentsCompany(generics.ListAPIView):
    serializer_class = DocumentsListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Documents.objects.filter(idcompany = pk)

    def list(self, request, pk=None):
        documents_serializer = self.serializer_class(self.get_queryset(), many = True)
        if(documents_serializer.data != []):
            return Response(documents_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay Datos'},status= status.HTTP_400_BAD_REQUEST);