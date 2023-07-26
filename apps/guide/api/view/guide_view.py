from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from apps.guide.models import *
from apps.guide.api.serializers.guide_serializer import *

class GuideViewSet(viewsets.ModelViewSet):
    serializer_class = GuideSerializer
    list_serializer_class = GuideListSerializer

    def get_queryset(self):
        return Guide.objects.all()

    def list(self, request):
        guide_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(guide_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'guide creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        guide =  Guide.objects.filter(idGuide = pk).first()
        if guide:
            guide_serializer = self.serializer_class(guide)
            return Response(guide_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        guide =  Guide.objects.filter(idGuide = pk).first()
        if guide:
            guide_serializer = self.serializer_class(guide,data = request.data)
            if guide_serializer.is_valid():
                guide_serializer.save()
                return Response({'message':'guide Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(guide_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        guide =  Guide.objects.filter(idGuide = pk).first()
        if guide:
            self.perform_destroy(self.get_object())
            return Response({'message':'Bodega Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class GuideLocationLatitudeView(generics.ListAPIView):
    serializer_class = GuideLocationLatitudeSerializer
    travel_serializer_class = TravelSerializer

    def get_queryset(self):
        return Guide.objects.all()

    def list(self, request, pk=None):
        origin  = []
        o = []
        destination  = []
        travel =  Travel.objects.filter(idtravel = pk).first()
        if travel:
            travel_serializer = self.travel_serializer_class(travel)
            data = travel_serializer.data
            for i in data['guide']:
                guide =  Guide.objects.filter(idGuide = i).first()
                guide_serialize = self.serializer_class(guide)
                if guide_serialize.data not in origin:
                    origin.append({
                        'lat': guide_serialize.data['Olatitude'],
                        'lng':guide_serialize.data['Olongitude']
                    })
                    destination.append({
                        'location': {
                            'lat': guide_serialize.data['Dlatitude'],
                            'lng':guide_serialize.data['Dlongitude']
                        }
                    })
                print(guide_serialize.data)
            for i in origin:
                if i not in o:
                    o.append(i)
            router = {
                'origin': o,
                'destination': destination
            }
            return Response(router, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

class GuideListFalseView(generics.ListAPIView):
    serializer_class = GuideListSerializer
    def get_queryset(self):
        return Guide.objects.all()

    def list(self, request, idcompany=None, iduser = None, idvehicle= None):
        guide = Guide.objects.filter(idcompany = idcompany,iduser = iduser,idvehicle = idvehicle, status= False)
        if(guide):
            guide_serializer = self.serializer_class(guide, many = True)
            return Response(guide_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

class GuideDeailView(generics.ListAPIView):
    serializer_class = GuideListViewSerializer
    def get_queryset(self):
        return Guide.objects.all()

    def list(self, request, pk = None):
        guide = Guide.objects.filter(idguide = pk).first()
        print(pk)
        if(guide):
            guide_serializer = self.serializer_class(guide)
            return Response(guide_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)


class GuideListTrueView(generics.ListAPIView):
    serializer_class = GuideListSerializer
    travel_serializer_class = TravelSerializer
    def get_queryset(self):
        return Guide.objects.all()

    def list(self, request, idcompany=None, iduser = None, idvehicle= None, pk=None):
        travel = Travel.objects.filter(idtravel = pk).first()
        result = []
        if travel:
            travel_serializer = self.travel_serializer_class(travel)
            for item in travel_serializer.data['guide']:
                guide = Guide.objects.filter(idguide= item).first()
                guide_serializer = self.serializer_class(guide)
                result.append(guide_serializer.data)
            return Response(result, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)


class TravelViewSet(viewsets.ModelViewSet):
    serializer_class = TravelSerializer
    list_serializer_class = TravelListSerializer

    def get_queryset(self):
        return Travel.objects.all()

    def list(self, request):
        travel_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(travel_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            for i in data['guide']:
                guide =  Guide.objects.filter(idGuide = i).first()
                if guide:
                    guide.status = True
                    guide.save()
            serializer.save()
            return Response({'message': 'Viaje creada correctmente'},status= status.HTTP_201_CREATED)
        return Response({'eee': 'serializer.errors'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        travel =  Travel.objects.filter(idtravel = pk).first()
        if travel:
            travel_serializer = self.serializer_class(travel)
            return Response(travel_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        travel =  Travel.objects.filter(idtravel = pk).first()
        if travel:
            travel_serializer = self.serializer_class(travel,data = request.data)
            if travel_serializer.is_valid():
                travel_serializer.save()
                return Response({'message':'Viaje Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(travel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        travel =  Travel.objects.filter(idtravel = pk).first()
        if travel:
            self.perform_destroy(self.get_object())
            return Response({'message':'Viaje Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class GuideContentViewSet(viewsets.ModelViewSet):
    serializer_class = GuideContentSerializer
    list_serializer_class = GuideContentListSerializer

    def get_queryset(self):
        return GuideContent.objects.all()

    def list(self, request):
        guideContent_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(guideContent_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contenido creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        guidecontent =  GuideContent.objects.filter(idguidecontent = pk).first()
        if guidecontent:
            guidecontent_serializer = self.serializer_class(guidecontent)
            return Response(guidecontent_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        guidecontent =  guidecontent.objects.filter(idguidecontent = pk).first()
        if guidecontent:
            guidecontent_serializer = self.serializer_class(guidecontent,data = request.data)
            if guidecontent_serializer.is_valid():
                guidecontent_serializer.save()
                return Response({'message':'Contenido Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(guidecontent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        guidecontent =  GuideContent.objects.filter(idguidecontent = pk).first()
        if guidecontent:
            self.perform_destroy(self.get_object())
            return Response({'message':'Contenido Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class GuideContentDetailTmpViewSet(viewsets.ModelViewSet):
    serializer_class = GuideContentDetailTmpSerializer
    list_serializer_class = GuideContentDetailTmpListSerializer

    def get_queryset(self):
        return GuideContentDetailTmp.objects.all()

    def list(self, request):
        guidecontentdetailtmp_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(guidecontentdetailtmp_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Detalle creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        guidecontentdetailtmp =  GuideContentDetailTmp.objects.filter(idguidecontentdetailtmp = pk).first()
        if guidecontentdetailtmp:
            guidecontentdetailtmp_serializer = self.serializer_class(guidecontentdetailtmp)
            return Response(guidecontentdetailtmp_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        guidecontentdetailtmp =  GuideContentDetailTmp.objects.filter(idguidecontentdetailtmp = pk).first()
        if guidecontentdetailtmp:
            guidecontentdetailtmp_serializer = self.serializer_class(guidecontentdetailtmp,data = request.data)
            if guidecontentdetailtmp_serializer.is_valid():
                guidecontentdetailtmp_serializer.save()
                return Response({'message':'Detalle Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(guidecontentdetailtmp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        guidecontentdetailtmp =  GuideContentDetailTmp.objects.filter(idguidecontentdetailtmp = pk).first()
        if guidecontentdetailtmp:
            self.perform_destroy(self.get_object())
            return Response({'message':'Contenido Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class GuideContentDetailViewSet(viewsets.ModelViewSet):
    serializer_class = GuideContentDetailSerializer
    list_serializer_class = GuideContentDetailListSerializer

    def get_queryset(self):
        return GuideContentDetail.objects.all()

    def list(self, request):
        guidecontentdetail_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(guidecontentdetail_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Detalle creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        guidecontentdetail =  GuideContentDetail.objects.filter(idguidecontentdetail = pk).first()
        if guidecontentdetail:
            guidecontentdetail_serializer = self.serializer_class(guidecontentdetail)
            return Response(guidecontentdetail_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        guidecontentdetail =  GuideContentDetail.objects.filter(idguidecontentdetail = pk).first()
        if guidecontentdetail:
            guidecontentdetail_serializer = self.serializer_class(guidecontentdetail,data = request.data)
            if guidecontentdetail_serializer.is_valid():
                guidecontentdetail_serializer.save()
                return Response({'message':'Detalle Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(guidecontentdetail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        guidecontentdetail =  GuideContentDetail.objects.filter(idguidecontentdetail = pk).first()
        if guidecontentdetail:
            self.perform_destroy(self.get_object())
            return Response({'message':'Contenido Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.all()

    def list(self, request):
        unit_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(unit_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Unidad creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        unit =  Unit.objects.filter(idunit = pk).first()
        if unit:
            unit_serializer = self.serializer_class(unit)
            return Response(unit_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        unit =  Unit.objects.filter(idunit = pk).first()
        if unit:
            unit_serializer = self.serializer_class(unit,data = request.data)
            if unit_serializer.is_valid():
                unit_serializer.save()
                return Response({'message':'Detalle Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(unit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        unit =  Unit.objects.filter(idunit = pk).first()
        if unit:
            self.perform_destroy(self.get_object())
            return Response({'message':'Contenido Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class InvoiceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceTypeSerializer

    def get_queryset(self):
        return InvoiceType.objects.all()

    def list(self, request):
        invoicetype_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(invoicetype_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo creado correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        invoicetype =  InvoiceType.objects.filter(idinvoicetype = pk).first()
        if invoicetype:
            invoicetype_serializer = self.serializer_class(invoicetype)
            return Response(invoicetype_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        invoicetype =  InvoiceType.objects.filter(idinvoicetype = pk).first()
        if invoicetype:
            invoicetype_serializer = self.serializer_class(invoicetype,data = request.data)
            if invoicetype_serializer.is_valid():
                invoicetype_serializer.save()
                return Response({'message':'Tipo Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(invoicetype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        invoicetype =  InvoiceType.objects.filter(idinvoicetype = pk).first()
        if invoicetype:
            self.perform_destroy(self.get_object())
            return Response({'message':'Contenido Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)