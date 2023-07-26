from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from apps.routes.models import (
    Cellars,
    Destinations,
    Tabulation,
    Bill,
    Concepts
)
from apps.guide.models import Guide
from apps.guide.api.serializers.guide_serializer import GuideSerializer
from apps.routes.api.serializers.router_serializes import (
    CellarsListSerializer,
    CellarsSerializer,
    DestinationsListSerializer,
    DestinationsSerializer,
    TabulationListSerializer,
    TabulationSerializer,
    ConceptsSerializer,
    BillListSerializer,
    BillSerializer
)

class CellarsViewSet(viewsets.ModelViewSet):
    serializer_class = CellarsSerializer
    list_serializer_class = CellarsListSerializer

    def get_queryset(self):
        return Cellars.objects.all()

    def list(self, request):
        cellars_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(cellars_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Bodega creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        cellars =  Cellars.objects.filter(idcellars = pk).first()
        if cellars:
            cellars_serializer = self.serializer_class(cellars)
            return Response(cellars_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        cellars =  Cellars.objects.filter(idcellars = pk).first()
        if cellars:
            if cellars:
                cellars_serializer = self.serializer_class(cellars,data = request.data)
                if cellars_serializer.is_valid():
                    cellars_serializer.save()
                    return Response({'message':'Bodega Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(cellars_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cellars =  Cellars.objects.filter(idcellars = pk).first()
        if cellars:
            self.perform_destroy(self.get_object())
            return Response({'message':'Bodega Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class DestinationViewSet(viewsets.ModelViewSet):
    serializer_class = DestinationsSerializer
    list_serializer_class = DestinationsListSerializer

    def get_queryset(self):
        return Destinations.objects.all()

    def list(self, request):
        destinations_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(destinations_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Destino creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        destinations =  Destinations.objects.filter(iddestinations = pk).first()
        if destinations:
            destinations_serializer = self.serializer_class(destinations)
            return Response(destinations_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        destinations =  Destinations.objects.filter(iddestinations = pk).first()
        if destinations:
            if destinations:
                destinations_serializer = self.serializer_class(destinations,data = request.data)
                if destinations_serializer.is_valid():
                    destinations_serializer.save()
                    return Response({'message':'destino Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(destinations_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        destinations =  Destinations.objects.filter(iddestinations = pk).first()
        if destinations:
            self.perform_destroy(self.get_object())
            return Response({'message':'Destino Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class TabulationViewSet(viewsets.ModelViewSet):
    serializer_class = TabulationSerializer
    list_serializer_class = TabulationListSerializer

    def get_queryset(self):
        return Tabulation.objects.all()

    def list(self, request):
        tabulation_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(tabulation_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Dato creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        tabulation =  Tabulation.objects.filter(idtabulation = pk).first()
        if tabulation:
            tabulation_serializer = self.serializer_class(tabulation)
            return Response(tabulation_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        tabulation =  Tabulation.objects.filter(idtabulation = pk).first()
        if tabulation:
            if tabulation:
                tabulation_serializer = self.serializer_class(tabulation, data = request.data)
                if tabulation_serializer.is_valid():
                    tabulation_serializer.save()
                    return Response({'message':'Dato Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(tabulation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        tabulation =  Tabulation.objects.filter(idtabulation = pk).first()
        if tabulation:
            self.perform_destroy(self.get_object())
            return Response({'message':'Dato Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class TabulationCompany(generics.ListAPIView):
    serializer_class = TabulationListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Tabulation.objects.filter(idcompany = pk)

    def list(self, request, pk=None):
        documents_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(documents_serializer.data, status=status.HTTP_200_OK)

class TabulationOriginDestination(generics.ListAPIView):
    serializer_class = TabulationListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        pk1 = self.kwargs['pk1']
        pk2 = self.kwargs['pk2']
        return Tabulation.objects.filter(idcompany = pk, idlocation=pk1, iddestinations=pk2)

    def list(self, request, pk=None,pk1=None,pk2=None):
        documents_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(documents_serializer.data, status=status.HTTP_200_OK)

class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    list_serializer_class = BillListSerializer

    def get_queryset(self):
        return Bill.objects.all()

    def list(self, request):
        bill_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(bill_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Dato creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        bill =  Bill.objects.filter(idbill = pk).first()
        if bill:
            bill_serializer = self.serializer_class(bill)
            return Response(bill_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        bill =  Bill.objects.filter(idbill = pk).first()
        if bill:
            if bill:
                bill_serializer = self.serializer_class(bill, data = request.data)
                if bill_serializer.is_valid():
                    bill_serializer.save()
                    return Response({'message':'Dato Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(bill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        bill =  Bill.objects.filter(idbill = pk).first()
        if bill:
            self.perform_destroy(self.get_object())
            return Response({'message':'Dato Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class BillCompany(generics.ListAPIView):
    serializer_class = BillListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        pk1 = self.kwargs['pk1']
        return Bill.objects.filter(idcompany = pk, idtabulation = pk1)

    def list(self, request, pk=None, pk1= None):
        bill_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(bill_serializer.data, status=status.HTTP_200_OK)

class ConceptsViewSet(viewsets.ModelViewSet):
    serializer_class = ConceptsSerializer

    def get_queryset(self):
        return Concepts.objects.all()

    def list(self, request):
        concepts_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(concepts_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Dato creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        concepts=  Concepts.objects.filter(idconcepts = pk).first()
        if concepts:
            concepts_serializer = self.serializer_class(concepts)
            return Response(concepts_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        concepts =  Concepts.objects.filter(idconcepts = pk).first()
        if concepts:
            if concepts:
                concepts_serializer = self.serializer_class(concepts, data = request.data)
                if concepts_serializer.is_valid():
                    concepts_serializer.save()
                    return Response({'message':'Dato Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(concepts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        concepts =  Concepts.objects.filter(idconcepts = pk).first()
        if concepts:
            self.perform_destroy(self.get_object())
            return Response({'message':'Dato Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class BillTabulation(generics.CreateAPIView):
    serializer_class = BillListSerializer
    serializer_class_Guide = GuideSerializer
    serializer_class_Tabulation = TabulationListSerializer

    def get_queryset(self):
        return Bill.objects.all()

    def create(self, request):
        dato = request.data
        #[5, 6]
        print(dato)
        respuesta = []
        for item in dato:
            guide = Guide.objects.filter(idguide = item).first()
            if guide:
                serializer_guide = self.serializer_class_Guide(guide)
                result = serializer_guide.data
                idcompany = result['idcompany']
                idlocation = result['idlocation']
                iddestinations = result['iddestinations']
                tabulation = Tabulation.objects.filter(idcompany = idcompany, idlocation= idlocation, iddestinations=iddestinations).first()
                if tabulation:
                    serializer_tabulation = self.serializer_class_Tabulation(tabulation)
                    tabulationresult = serializer_tabulation.data
                    idtabulation = tabulationresult['idtabulation']
                    bill = Bill.objects.filter(idcompany = idcompany, idtabulation = idtabulation)
                    if bill:
                        serializer_class_bill = self.serializer_class(bill, many = True)
                        for i in serializer_class_bill.data:
                            respuesta.append(i)
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0
        sum6 = 0
        sum7 = 0
        idcompany = 0
        ressult1 = []
        for r in respuesta:
            if r['concepts'] == 'DIESEL':
                sum1 += r['amount']
            if r['concepts'] == 'PEAJE':
                sum2 += r['amount']
            if r['concepts'] == 'VIÁTICOS':
                sum3 += r['amount']
            if r['concepts'] == 'PESAS Y BALANZA':
                sum4 += r['amount']
            if r['concepts'] == 'CARGUE Y DESCARGUE':
                sum5 += r['amount']
            if r['concepts'] == 'CARAVANA':
                print(r)
                sum6 += r['amount']
            idcompany = r['idcompany']
        dato1 = {
            'concepts': 'DIESEL',
            'amount': sum1,
            'idcompany': idcompany
        }
        ressult1.append(dato1)
        dato2 = {
            'concepts': 'PEAJE',
            'amount': sum2,
            'idcompany': idcompany
        }
        ressult1.append(dato2)
        dato3 = {
            'concepts': 'VIÁTICOS',
            'amount': sum3,
            'idcompany': idcompany
        }
        ressult1.append(dato3)
        dato4 = {
            'concepts': 'PESAS Y BALANZA',
            'amount': sum4,
            'idcompany': idcompany
        }
        ressult1.append(dato4)
        dato5 = {
            'concepts': 'CARGUE Y DESCARGUE',
            'amount': sum5,
            'idcompany': idcompany
        }
        ressult1.append(dato5)
        dato6 = {
            'concepts': 'CARAVANA',
            'amount': sum6,
            'idcompany': idcompany
        }
        ressult1.append(dato6)
        #return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ressult1, status=status.HTTP_200_OK)

