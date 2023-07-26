import re
from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from apps.vehicle.models import FixedCosts, TechnicalData, Vehicle, VehicleModel, TechnicalDataTrailer,Trailer, DocumentVehicle, AssignTrailer
from apps.vehicle.api.serializers.vehicle_serializers import (
    FixedCostsSerializer,
    TechnicalDataSerializer,
    TechnicalDataListSerializer,
    VehicleModelSerializer,
    VehicleModelListSerializer,
    VehicleSerializer,
    VehicleListSerializer,
    VehicleViewSerializer,
    TrailerSerializer,
    TrailerListSerializer,
    TechnicalDataTrailerSerializer,
    TechnicalDataTrailerListSerializer,
    TrailerViewSerializer,
    DocumentVehicleListSerializer,
    DocumentVehicleSerializer,
    AssignTrailerSerializer
    )

class TechnicalDataViewSet(viewsets.ModelViewSet):
    serializer_class = TechnicalDataSerializer
    list_serializer_class = TechnicalDataListSerializer

    def get_queryset(self):
        return TechnicalData.objects.all()

    def list(self, request):
        technicaldata_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(technicaldata_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos tecnicos creados correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        technicaldata =  TechnicalData.objects.filter(idtechnical_data = pk).first()
        if technicaldata:
            technicaldata_serializer = self.serializer_class(technicaldata)
            return Response(technicaldata_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        technicaldata =  TechnicalData.objects.filter(idtechnical_data = pk).first()
        if technicaldata:
            if technicaldata:
                technicaldata_serializer = self.serializer_class(technicaldata,data = request.data)
                if technicaldata_serializer.is_valid():
                    technicaldata_serializer.save()
                    return Response({'message':'Datos tecnicos Actualizados Correctamente'}, status=status.HTTP_200_OK)
            return Response(technicaldata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        technicaldata =  TechnicalData.objects.filter(idtechnical_data = pk).first()
        if technicaldata:
            self.perform_destroy(self.get_object())
            return Response({'message':'Datos tecnicos Eliminados Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class VehicleModelViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleModelSerializer
    list_serializer_class = VehicleModelListSerializer

    def get_queryset(self):
        return VehicleModel.objects.all()

    def list(self, request):
        vehiclemodel_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response( vehiclemodel_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Modelo del Vehiculo creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        vehiclemodel =  VehicleModel.objects.filter(idvehicle_model = pk).first()
        if vehiclemodel:
            vehiclemodel_serializer = self.serializer_class(vehiclemodel)
            return Response(vehiclemodel_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        vehiclemodel =  VehicleModel.objects.filter(idvehicle_model = pk).first()
        if vehiclemodel:
            if vehiclemodel:
                vehiclemodel_serializer = self.serializer_class(vehiclemodel,data = request.data)
                if vehiclemodel_serializer.is_valid():
                    vehiclemodel_serializer.save()
                    return Response({'message':'Modelo del Vehiculo Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(vehiclemodel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        vehiclemodel =  VehicleModel.objects.filter(idvehicle_model = pk).first()
        if vehiclemodel:
            self.perform_destroy(self.get_object())
            return Response({'message':'Modelo del Vehiculo Eliminados Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    list_serializer_class = VehicleListSerializer

    def get_queryset(self):
        #string = self.request.META['QUERY_STRING']
        #s = [int(s) for s in re.findall(r'-?\d+\.?\d*', string)]
        #id = s[0]
        return Vehicle.objects.all()

    def list(self, request):
        vehicle_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(vehicle_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Vehiculo creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        vehicle =  Vehicle.objects.filter(idvehicle = pk).first()
        if vehicle:
            vehicle_serializer = self.serializer_class(vehicle)
            return Response(vehicle_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        vehicle =  Vehicle.objects.filter(idvehicle = pk).first()
        print(request.data)
        if vehicle:
            if vehicle:
                vehicle_serializer = self.serializer_class(vehicle,data = request.data)
                if vehicle_serializer.is_valid():
                    vehicle_serializer.save()
                    return Response({'message':'Vehiculo Actualizado Correctamente'}, status=status.HTTP_200_OK)
            print(vehicle_serializer.errors)# type: ignore
            return Response(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        vehicle =  Vehicle.objects.filter(idvehicle = pk).first()
        if vehicle:
            self.perform_destroy(self.get_object())
            return Response({'message':'Vehiculo Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class CreateVehicle(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    serializer_class1 = TechnicalDataSerializer
    serializer_class_List = VehicleViewSerializer

    def get_queryset(self):
        return Vehicle.objects.all()

    def list(self, request):
        vehicle_serialize =  self.serializer_class_List(self.get_queryset(), many = True)
        return Response(vehicle_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        load_capacity = request.data['load_capacity']
        color = request.data['color']
        mileage = request.data['mileage']
        idfuel = request.data['idfuel']
        year = request.data['year']
        idgps = request.data['idgps']
        agination_date = request.data['agination_date']
        tuition = request.data['tuition']
        engine_series = request.data['engine_series']
        state = request.data['state']
        idowner = request.data['idowner']
        idvehicle_model = request.data['idvehicle_model']
        idemployee = request.data['idemployee']
        idvehicle_use = request.data['idvehicle_use']
        hours_use = request.data['hours_use']
        tank_capacity = request.data['tank_capacity']
        yield_gallon = request.data['yield_gallon']
        observation = request.data['observation']
        data = {
            "load_capacity": load_capacity,
            "color": color,
            "mileage":mileage,
            "idfuel":idfuel,
            "hours_use": hours_use,
            "tank_capacity": tank_capacity,
            "yield_gallon": yield_gallon,
            "observation": observation,
            "year": year,
            "idgps":idgps
        }

        serializer = self.serializer_class1(data = data)# type: ignore
        if serializer.is_valid():
            serializer.save()
            d = serializer.data['idtechnical_data']

            if(request.data['image']):
                 data1 = {
                    "agination_date": agination_date,
                    "image": request.data['image'],
                    "tuition": tuition,
                    "engine_series": engine_series,
                    "state": state,
                    "idowner": idowner,
                    "idvehicle_model": idvehicle_model,
                    "idemployee": idemployee,
                    "idvehicle_use": idvehicle_use,
                    "idtechnical_data": d
                }
            else:
                data1 = {
                "agination_date": agination_date,
                "tuition": tuition,
                "engine_series": engine_series,
                "state": state,
                "idowner": idowner,
                "idvehicle_model": idvehicle_model,
                "idemployee": idemployee,
                "idvehicle_use": idvehicle_use,
                "idtechnical_data": d
            }
            serializer1 = self.serializer_class(data=data1) # type: ignore
            if serializer1.is_valid():
                serializer1.save()
                return Response({'message': 'Produco creado correctmente'},status= status.HTTP_201_CREATED)
            return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechnicalDataTrailerViewSet(viewsets.ModelViewSet):
    serializer_class = TechnicalDataTrailerSerializer
    list_serializer_class = TechnicalDataTrailerListSerializer

    def get_queryset(self):
        return TechnicalDataTrailer.objects.all()

    def list(self, request):
        technicaldatatrailer_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(technicaldatatrailer_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos tecnicos creados correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        technicaldatatrailer =  TechnicalDataTrailer.objects.filter(idtechnical_datatrailer = pk).first()
        if technicaldatatrailer:
            technicaldata_serializer = self.serializer_class(technicaldatatrailer)
            return Response(technicaldata_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        technicaldatatrailer =  TechnicalDataTrailer.objects.filter(idtechnical_datatrailer = pk).first()
        if technicaldatatrailer:
            if technicaldatatrailer:
                technicaldatatrailer_serializer = self.serializer_class(technicaldatatrailer,data = request.data)
                if technicaldatatrailer_serializer.is_valid():
                    technicaldatatrailer_serializer.save()
                    return Response({'message':'Datos tecnicos Actualizados Correctamente'}, status=status.HTTP_200_OK)
            return Response(technicaldatatrailer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        technicaldatatrailer =  TechnicalDataTrailer.objects.filter(idtechnical_datatrailer = pk).first()
        if technicaldatatrailer:
            self.perform_destroy(self.get_object())
            return Response({'message':'Datos tecnicos Eliminados Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class TrailerViewSet(viewsets.ModelViewSet):
    serializer_class = TrailerSerializer
    list_serializer_class = TrailerListSerializer
    def get_queryset(self):
        return Trailer.objects.all()

    def list(self, request):
        trailer_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(trailer_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Remolque creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        trailer =  Trailer.objects.filter(idtrailer = pk).first()
        if trailer:
            trailer_serializer = self.serializer_class(trailer)
            return Response(trailer_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        trailer =  Trailer.objects.filter(idtrailer = pk).first()
        print(request.data)
        if trailer:
            if trailer:
                trailer_serializer = self.serializer_class(trailer,data = request.data)
                if trailer_serializer.is_valid():
                    trailer_serializer.save()
                    return Response({'message':'Remolque Actualizado Correctamente'}, status=status.HTTP_200_OK)
            print(trailer_serializer.errors)# type: ignore
            return Response(trailer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        trailer =  Trailer.objects.filter(idtrailer = pk).first()
        if trailer:
            self.perform_destroy(self.get_object())
            return Response({'message':'Vehiculo Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class CreateTrailer(generics.ListCreateAPIView):
    serializer_class = TrailerSerializer
    serializer_class1 = TechnicalDataTrailerSerializer
    serializer_class_List = TrailerViewSerializer


    def get_queryset(self):
        return Trailer.objects.all()

    def list(self, request):
        vehicle_serialize =  self.serializer_class_List(self.get_queryset(), many = True)
        return Response(vehicle_serialize.data, status=status.HTTP_200_OK)
        return

    def create(self, request):
        load_capacity = request.data['load_capacity']
        color = request.data['color']
        idadministrative_data = request.data['idadministrative_data']
        tuition = request.data['tuition']
        state = request.data['state']
        idowner = request.data['idowner']
        idvehicle_model = request.data['idvehicle_model']
        idvehicle_use = request.data['idvehicle_use']
        hours_use = request.data['hours_use']
        observation = request.data['observation']

        data = {
            "load_capacity": load_capacity,
            "color": color,
            "hours_use": hours_use,
            "observation": observation,
            "idadministrative_data":idadministrative_data,
        }
        serializer = self.serializer_class1(data = data)# type: ignore
        if serializer.is_valid():
            serializer.save()
            d = serializer.data['idtechnical_datatrailer']

            if(request.data['image']):
                 data1 = {
                    "image": request.data['image'],
                    "tuition": tuition,
                    "state": state,
                    "idowner": idowner,
                    "idvehicle_model": idvehicle_model,
                    "idvehicle_use": idvehicle_use,
                    "idtechnical_datatrailer": d
                }
            else:
                data1 = {
                "tuition": tuition,
                "state": state,
                "idowner": idowner,
                "idvehicle_model": idvehicle_model,
                "idvehicle_use": idvehicle_use,
                "idtechnical_datatrailer": d
            }
            serializer1 = self.serializer_class(data=data1) # type: ignore
            if serializer1.is_valid():
                serializer1.save()
                return Response({'message': 'Produco creado correctmente'},status= status.HTTP_201_CREATED)
            return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentVehicleViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentVehicleSerializer
    List_serializer_class = DocumentVehicleListSerializer

    def get_queryset(self):
        return DocumentVehicle.objects.all()

    def list(self, request):
        documentvehicle_serialize =  self.List_serializer_class(self.get_queryset(), many = True)
        return Response(documentvehicle_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Creado Correctamente'},status= status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        documentvehicle =  DocumentVehicle.objects.filter(iddocument_vehicle = pk).first()
        if documentvehicle:
            documentemployee_serializer = self.serializer_class(documentvehicle)
            return Response(documentemployee_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        documentvehicle =  DocumentVehicle.objects.filter(iddocument_vehicle = pk).first()
        if documentvehicle:
            if documentvehicle:
                documentvehicle_serializer = self.serializer_class(documentvehicle,data = request.data)
                if documentvehicle_serializer.is_valid():
                    documentvehicle_serializer.save()
                    return Response({'message':'Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(documentvehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        documentvehicle = DocumentVehicle.objects.filter(iddocument_vehicle = pk).first()
        if documentvehicle:
            self.perform_destroy(self.get_object())
            return Response({'message':'Documento Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)


class DocumentsVehicle(generics.ListAPIView):
    serializer_class = DocumentVehicleListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return DocumentVehicle.objects.filter(idvehicle = pk)

    def list(self, reques,pk=None):
        documentvehicle_serializer = self.serializer_class(self.get_queryset(), many = True)
        if(documentvehicle_serializer.data != []):
            return Response(documentvehicle_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay Datos'},status= status.HTTP_400_BAD_REQUEST);

class AssignTrailerViewSet(viewsets.ModelViewSet):
    serializer_class = AssignTrailerSerializer

    def get_queryset(self):
        return AssignTrailer.objects.all()

    def list(self, request):
        vehicle_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(vehicle_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Asignacion  creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        assigntrailer =  AssignTrailer.objects.filter(idassigntrailer = pk).first()
        if assigntrailer:
            assigntrailer_serializer = self.serializer_class(assigntrailer)
            return Response(assigntrailer_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        assigntrailer =  AssignTrailer.objects.filter(idassigntrailer = pk).first()
        print(request.data)
        if assigntrailer:
            if assigntrailer:
                assigntrailer_serializer = self.serializer_class(assigntrailer,data = request.data)
                if assigntrailer_serializer.is_valid():
                    assigntrailer_serializer.save()
                    return Response({'message':'Asignacion Actualizada Actualizado Correctamente'}, status=status.HTTP_200_OK)
            print(vehicle_serializer.errors)# type: ignore
            return Response(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        assigntrailer =  AssignTrailer.objects.filter(idassigntrailer = pk).first()
        if assigntrailer:
            self.perform_destroy(self.get_object())
            return Response({'message':'Agignacion Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class AssignVehicleTrailer(generics.ListAPIView):
    serializer_class = AssignTrailerSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return AssignTrailer.objects.filter(idvehicle = pk)

    def list(self, reques,pk=None):
        assigntrailer_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response( assigntrailer_serializer.data, status=status.HTTP_200_OK)

class FixedCostsViewSet(viewsets.ModelViewSet):
    serializer_class = FixedCostsSerializer

    def get_queryset(self):
        return FixedCosts.objects.all()

    def list(self, request):
        fixedcosts_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(fixedcosts_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Creado Correctamente'},status= status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        fixedcosts =  FixedCosts.objects.filter(idfixedcosts = pk).first()
        if fixedcosts:
            fixedcosts_serializer = self.serializer_class(fixedcosts)
            return Response(fixedcosts_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        fixedcosts =  FixedCosts.objects.filter(idfixedcosts = pk).first()
        if fixedcosts:
            if fixedcosts:
                fixedcosts_serializer = self.serializer_class(fixedcosts,data = request.data)
                if fixedcosts_serializer.is_valid():
                    fixedcosts_serializer.save()
                    return Response({'message':'Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(fixedcosts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        fixedcosts = FixedCosts.objects.filter(idfixedcosts = pk).first()
        if fixedcosts:
            self.perform_destroy(self.get_object())
            return Response({'message':'Costos Fijos Eliminados Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class FixedCostsVehicle(generics.ListAPIView):
    serializer_class = FixedCostsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return FixedCosts.objects.filter(idvehicle = pk)

    def list(self, reques,pk=None):
        fixedcosts_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response( fixedcosts_serializer.data, status=status.HTTP_200_OK)