from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.employees.models import DocumentType, PeriodPayment, PositionType, Position, LaborPayments
from apps.employees.api.serializers.general_serializers import EmployeesDocumentTypeSerializer, PeriodPaymentSerializer, PositionTypeSerializer, PositionSerializer, LaborPaymentsSerializer, PositionListSerializer

class DocumentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeesDocumentTypeSerializer

    def get_queryset(self):
        return DocumentType.objects.all()

    def list(self, request):
        documenttype_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(documenttype_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Documento Creado Correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        documenttype =  DocumentType.objects.filter(iddocument_type = pk).first()
        if documenttype:
            documenttype_serializer = self.serializer_class(documenttype)
            return Response(documenttype_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        documenttype =  DocumentType.objects.filter(iddocument_type = pk).first()
        if documenttype:
            if documenttype:
                documenttype_serializer = self.serializer_class(documenttype,data = request.data)
                if documenttype_serializer.is_valid():
                    documenttype_serializer.save()
                    return Response({'message':'Documento Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(documenttype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        documenttype = DocumentType.objects.filter(iddocument_type = pk).first()
        if documenttype:
            self.perform_destroy(self.get_object())
            return Response({'message':'Documento Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class PeriodPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodPaymentSerializer

    def get_queryset(self):
        return PeriodPayment.objects.all()

    def list(self, request):
        periodpayment_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(periodpayment_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Periodo de Pago Creado Correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        periodpayment =  PeriodPayment.objects.filter(idperiod_payment = pk).first()
        if periodpayment:
            periodpayment_serializer = self.serializer_class(periodpayment)
            return Response(periodpayment_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        periodpayment =  PeriodPayment.objects.filter(idperiod_payment = pk).first()
        if periodpayment:
            if periodpayment:
                periodpayment_serializer = self.serializer_class(periodpayment,data = request.data)
                if periodpayment_serializer.is_valid():
                   periodpayment_serializer.save()
                   return Response({'message':'Periodo de Pago Correctamente'}, status=status.HTTP_200_OK)
            return Response(periodpayment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        periodpayment = PeriodPayment.objects.filter(idperiod_payment = pk).first()
        if periodpayment:
            self.perform_destroy(self.get_object())
            return Response({'message':'Periodo de Pago Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class PositionTypeViewSet(viewsets.ModelViewSet):
    serializer_class = PositionTypeSerializer

    def get_queryset(self):
        return PositionType.objects.all()

    def list(self, request):
        positiontype_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(positiontype_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de Puesto Creado Correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        positiontype =  PositionType.objects.filter(idposition_type = pk).first()
        if positiontype:
            positiontype_serializer = self.serializer_class(positiontype)
            return Response(positiontype_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        positiontype =  PositionType.objects.filter(idposition_type = pk).first()
        if positiontype:
            if positiontype:
                positiontype_serializer = self.serializer_class(positiontype,data = request.data)
                if positiontype_serializer.is_valid():
                   positiontype_serializer.save()
                   return Response({'message':'Tipo de puesto de trabajo Creado Correctamente'}, status=status.HTTP_200_OK)
            return Response(positiontype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        positiontype = PositionType.objects.filter(idposition_type = pk).first()
        if positiontype:
            self.perform_destroy(self.get_object())
            return Response({'message':'Tipo de Puesto de trabajo eliminado Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    List_serializer_class = PositionListSerializer

    def get_queryset(self):
        return Position.objects.all()

    def list(self, request):
        position_serialize =  self.List_serializer_class(self.get_queryset(), many = True)
        return Response(position_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Puesto Creado Correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        position =  Position.objects.filter(idposition = pk).first()
        if position:
            position_serializer = self.serializer_class(position)
            return Response(position_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        position =  Position.objects.filter(idposition = pk).first()
        if position:
            if position:
                position_serializer = self.serializer_class(position,data = request.data)
                if position_serializer.is_valid():
                   position_serializer.save()
                   return Response({'message':'Puesto de trabajo Creado Correctamente'}, status=status.HTTP_200_OK)
            return Response(position_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        position = Position.objects.filter(idposition = pk).first()
        if position:
            self.perform_destroy(self.get_object())
            return Response({'message':'Puesto de trabajo eliminado Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class LaborPaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = LaborPaymentsSerializer

    def get_queryset(self):
        return LaborPayments.objects.all()


