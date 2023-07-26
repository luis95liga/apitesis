from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from apps.vehicle.models import (
    Owner,
    VehicleUse,
    Axes,
    Manufacturer,
    VehicleType,
    Fuel,
    GeneralData,
    MaintenamceCosts,
    DocumentType
)
from apps.vehicle.api.serializers.general_serializers import (
    OwnerSerializer,
    OwnerListSerializer,
    VehicleUseSerializer,
    AxesSerializer,
    ManufacturerSerializer,
    VehicleTypeSerializer,
    FuelSerializer,
    GeneralDataSerializer,
    MaintenamceCostsSerializer,
    VehicleDocumentTypeSerializer
    )

class DocumentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleDocumentTypeSerializer

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

class OwnerViewSet(viewsets.ModelViewSet):
    serializer_class = OwnerSerializer
    list_serializer_class = OwnerListSerializer

    def get_queryset(self):
        return Owner.objects.all()
    
    def list(self, request):
        owner_serialize = self.list_serializer_class(self.get_queryset(), many = True)
        return Response(owner_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Propietario creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        owner =  Owner.objects.filter(idowner = pk).first()
        if owner:
            owner_serializer = self.serializer_class(owner)
            return Response(owner_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        owner =  Owner.objects.filter(idowner = pk).first()
        print(request.data)
        if owner:
            if owner:
                owner_serializer = self.serializer_class(owner,data = request.data)
                if owner_serializer.is_valid():
                    owner_serializer.save()
                    return Response({'message': 'Propietario actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(owner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        owner =  Owner.objects.filter(idowner = pk).first()
        if owner:
            self.perform_destroy(self.get_object())
            return Response({'message':'Propietario Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class VehicleUseViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleUseSerializer

    def get_queryset(self):
        return VehicleUse.objects.all()
    
    def list(self, request):
        vehicleuse_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(vehicleuse_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Uso de Vehiculo creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        vehicleuse =  VehicleUse.objects.filter(idvehicle_use = pk).first()
        if vehicleuse:
            vehicleuse_serializer = self.serializer_class(vehicleuse)
            return Response(vehicleuse_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        vehicleuse =  VehicleUse.objects.filter(idvehicle_use = pk).first()
        print(request.data)
        if vehicleuse:
            if vehicleuse:
                vehicleuse_serializer = self.serializer_class(vehicleuse,data = request.data)
                if vehicleuse_serializer.is_valid():
                    vehicleuse_serializer.save()
                    return Response({'message': 'Propietario actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(vehicleuse_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        vehicleuse =  VehicleUse.objects.filter(idvehicle_use = pk).first()
        if vehicleuse:
            self.perform_destroy(self.get_object())
            return Response({'message':'Propietario Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)


class AxesViewSet(viewsets.ModelViewSet):
    serializer_class = AxesSerializer

    def get_queryset(self):
        return Axes.objects.all()
    
    def list(self, request):
        vehicleuse_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(vehicleuse_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Eje creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        axes =  Axes.objects.filter(idaxis = pk).first()
        if axes:
            axes_serializer = self.serializer_class(axes)
            return Response(axes_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        axes =  Axes.objects.filter(idaxis = pk).first()
        print(request.data)
        if axes:
            if axes:
                axes_serializer = self.serializer_class(axes,data = request.data)
                if axes_serializer.is_valid():
                    axes_serializer.save()
                    return Response({'message': 'Eje actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(axes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        vehicleuse =  Axes.objects.filter(idaxis = pk).first()
        if vehicleuse:
            self.perform_destroy(self.get_object())
            return Response({'message':'Eje Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        return Manufacturer.objects.all()

    def list(self, request):
        manufacturer_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(manufacturer_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Fabricante creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        manufacturer =  Manufacturer.objects.filter(idmanufacturer = pk).first()
        if manufacturer:
            manufacturer_serializer = self.serializer_class(manufacturer)
            return Response(manufacturer_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        manufacturer =  Manufacturer.objects.filter(idmanufacturer = pk).first()
        print(request.data)
        if manufacturer:
            if manufacturer:
                manufacturer_serializer = self.serializer_class(manufacturer,data = request.data)
                if manufacturer_serializer.is_valid():
                    manufacturer_serializer.save()
                    return Response({'message': 'Fabricante actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(manufacturer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        manufacturer =  Manufacturer.objects.filter(idmanufacturer = pk).first()
        if manufacturer:
            self.perform_destroy(self.get_object())
            return Response({'message':'Fabricante Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class VehicleTypeViewSet(viewsets.ModelViewSet): 
    serializer_class = VehicleTypeSerializer
    def get_queryset(self):
        return VehicleType.objects.all()

    def list(self, request):
        vehicletype_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(vehicletype_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de Vehiculo creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        vehicletype =  VehicleType.objects.filter(idvehicle_type = pk).first()
        if vehicletype:
            vehicletype_serializer = self.serializer_class(vehicletype)
            return Response(vehicletype_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        vehicletype =  VehicleType.objects.filter(idvehicle_type = pk).first()
        print(request.data)
        if vehicletype:
            if vehicletype:
                vehicletype_serializer = self.serializer_class(vehicletype,data = request.data)
                if vehicletype_serializer.is_valid():
                    vehicletype_serializer.save()
                    return Response({'message': 'Tipo de Vehiculo actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(vehicletype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        vehicletype =  VehicleType.objects.filter(idvehicle_type = pk).first()
        if vehicletype:
            self.perform_destroy(self.get_object())
            return Response({'message':'Tipo de vehiculo Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class FuelViewSet(viewsets.ModelViewSet):
    serializer_class = FuelSerializer
    def get_queryset(self):
        return Fuel.objects.all()

    def list(self, request):
        fuel_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(fuel_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Combustible creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        fuel =  Fuel.objects.filter(idfuel = pk).first()
        if fuel:
            fuel_serializer = self.serializer_class(fuel)
            return Response(fuel_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        fuel =  Fuel.objects.filter(idfuel = pk).first()
        print(request.data)
        if fuel:
            if fuel:
                fuel_serializer = self.serializer_class(fuel,data = request.data)
                if fuel_serializer.is_valid():
                    fuel_serializer.save()
                    return Response({'message': 'Combustible actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(fuel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        fuel =  Fuel.objects.filter(idfuel = pk).first()
        if fuel:
            self.perform_destroy(self.get_object())
            return Response({'message':'Combustible Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class GeneralDataViewSet(viewsets.ModelViewSet):
    serializer_class = GeneralDataSerializer
    
    def get_queryset(self):
        return GeneralData.objects.all()

    def list(self, request):
        generaldata_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(generaldata_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos Generales creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk = None):
        generaldata =  GeneralData.objects.filter(idgeneraldata = pk).first()
        if generaldata:
            generaldata_serializer = self.serializer_class(generaldata)
            return Response(generaldata_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        generaldata =  GeneralData.objects.filter(idgeneraldata = pk).first()
        print(request.data)
        if generaldata:
            if generaldata:
                generaldata_serializer = self.serializer_class(generaldata,data = request.data)
                if generaldata_serializer.is_valid():
                    generaldata_serializer.save()
                    return Response({'message': 'Datos Generales actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(generaldata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        generaldata =  GeneralData.objects.filter(idgeneraldata = pk).first()
        if generaldata:
            self.perform_destroy(self.get_object())
            return Response({'message':'Datos Generales Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class GeneralDataVehicle(generics.ListAPIView):
    serializer_class = GeneralDataSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return GeneralData.objects.filter(idvehicle = pk)

    def list(self, request, pk=None):
        vehicle_serializer = self.serializer_class(self.get_queryset(), many = True)
        if(vehicle_serializer.data != []):
            return Response(vehicle_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay Datos'},status= status.HTTP_200_OK);

class MaintenamceCostsViewSet(viewsets.ModelViewSet):
    serializer_class = MaintenamceCostsSerializer
    
    def get_queryset(self):
        return MaintenamceCosts.objects.all()

    def list(self, request):
        maintenamcecosts_serialize = self.serializer_class(self.get_queryset(), many = True)
        return Response(maintenamcecosts_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos Generales creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        maintenamcecosts =  MaintenamceCosts.objects.filter(idmaintenamceCosts = pk).first()
        if maintenamcecosts:
            maintenamcecosts_serializer = self.serializer_class(maintenamcecosts)
            return Response(maintenamcecosts_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        maintenamcecosts =  MaintenamceCosts.objects.filter(idmaintenamceCosts = pk).first()
        if maintenamcecosts:
            if maintenamcecosts:
                maintenamcecosts_serializer = self.serializer_class(maintenamcecosts,data = request.data)
                if maintenamcecosts_serializer.is_valid():
                    maintenamcecosts_serializer.save()
                    return Response({'message': 'Datos Generales actualizado correctmente'}, status=status.HTTP_200_OK)
            return Response(maintenamcecosts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        maintenamcecosts =  MaintenamceCosts.objects.filter(idmaintenamceCosts = pk).first()
        if maintenamcecosts:
            self.perform_destroy(self.get_object())
            return Response({'message':'Datos Generales Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class MaintenamceCostsVehicle(generics.ListAPIView):
    serializer_class = MaintenamceCostsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return MaintenamceCosts.objects.filter(idvehicle = pk)

    def list(self, request, pk=None):
        maintenamcecosts_serializer = self.serializer_class(self.get_queryset(), many = True)
        if(maintenamcecosts_serializer.data != []):
            return Response(maintenamcecosts_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay Datos'},status= status.HTTP_200_OK);