import decimal
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from apps.guide.models import Guide, Travel
from apps.vehicle.models import Vehicle, Trailer,GeneralData, FixedCosts, MaintenamceCosts
from apps.vehicle.api.serializers.vehicle_serializers import VehicleListSerializer, VehicleSerializer , TrailerListSerializer, TrailerSerializer, FixedCostsSerializer
from apps.vehicle.api.serializers.general_serializers import GeneralDataSerializer, MaintenamceCostsSerializer
from apps.employees.models import Employee
from apps.employees.api.serializers.employee_serializers import EmployeeSerializer
from apps.guide.api.serializers.guide_serializer import GuideLocationLatitudeSerializer, GuideSerializer,GuideListSerializer, TravelListSerializer, TravelSerializer
from apps.company.api.serializers.company_serializes import CompanySerializer
from apps.company.models import Company
from apps.routes.models import Bill, Tabulation
from apps.routes.api.serializers.router_serializes import BillListSerializer, TabulationListSerializer
from decimal import Decimal

class ReportPdf(generics.ListAPIView):
    serializer_class = TravelSerializer
    list_serializer_class = TravelListSerializer
    vehicle_serializer_class = VehicleListSerializer
    trailer_serializer_class = TrailerListSerializer
    guide_list_serializer_class = GuideListSerializer
    guide_serializer_class = GuideSerializer
    generaldata_serializer_class = GeneralDataSerializer
    employee_serializer_class = EmployeeSerializer
    fixedcosts_serializer_class = FixedCostsSerializer
    company_serializer_class = CompanySerializer
    maintenamceCosts_serializer_class = MaintenamceCostsSerializer
    bill_serializer_class = BillListSerializer
    tabulation_serializer_class = TabulationListSerializer

    def get_queryset(self):
        return Travel.objects.all()

    def list(self, request, pk= None, idcompany= None):
        travel = Travel.objects.filter(idtravel = pk).first()
        if(travel):
            travel_serializer = self.serializer_class(travel)
            idvehicle = travel_serializer.data['idvehicle']
            idtrailer = travel_serializer.data['idtrailer']
            vehicle = Vehicle.objects.filter( idvehicle= idvehicle).first()
            vehicle_serializer =  self.vehicle_serializer_class(vehicle)
            trailer = Trailer.objects.filter(idtrailer=idtrailer).first()
            trailer_serializer = self.trailer_serializer_class(trailer)
            dataguide = travel_serializer.data['guide']
            location = []
            destinations = []
            client = []
            respuesta = []
            for i in dataguide:
                  guide =  Guide.objects.filter(idguide = i).first()
                  guide_list_serialize = self.guide_list_serializer_class(guide)
                  guide_serialize = self.guide_serializer_class(guide)
                  idlocation = guide_serialize.data['idlocation']
                  iddestinations = guide_serialize.data['iddestinations']
                  tabulation = Tabulation.objects.filter(idcompany = idcompany, idlocation= idlocation, iddestinations=iddestinations).first()
                  serializer_tabulation = self.tabulation_serializer_class(tabulation)
                  tabulationresult = serializer_tabulation.data
                  idtabulation = tabulationresult['idtabulation']
                  bill = Bill.objects.filter(idcompany = idcompany, idtabulation = idtabulation)
                  bill_serializer = self.bill_serializer_class(bill, many = True)
                  for i in bill_serializer.data:
                        respuesta.append(i)
                  location.append(guide_list_serialize.data['location'])
                  destinations.append(guide_list_serialize.data['destinations'])
                  client.append(guide_list_serialize.data['client'])
            o=[]
            d=[]
            c=[]
            for i in location:
                if i not in o:
                    o.append(i)
            for i in destinations:
                if i not in d:
                    d.append(i)
            for i in client:
                if i not in c:
                    c.append(i)
            idemployee = vehicle_serializer.data['idemployee']
            employee = Employee.objects.filter(idemployee = idemployee).first()
            employee_serializer = self.employee_serializer_class(employee)
            generaldata = GeneralData.objects.filter(idvehicle = idvehicle).first()
            generaldata_serializer = self.generaldata_serializer_class(generaldata)
            travelsalary =  float(employee_serializer.data['salary'])
            fixedcosts = FixedCosts.objects.filter(idvehicle = idvehicle).first()
            fixedcosts_serializer = self.fixedcosts_serializer_class(fixedcosts)
            company = Company.objects.filter(idcompany = idcompany).first()
            company_serializer = self.company_serializer_class(company)
            loadVehicle = int(company_serializer.data['default_load_type'])
            TKmM =  float(generaldata_serializer.data['ntravelkmmonth'])*(( float(travel_serializer.data['kms']) + float(travel_serializer.data['kmsdes']))*2)
            salaryKm = travelsalary/TKmM
            garageKm = (float(generaldata_serializer.data['garage'])/TKmM)
            registrationKm = ((float(fixedcosts_serializer.data['vehicleRegistration'])/12)/TKmM)
            sureKm = (float(fixedcosts_serializer.data['insurance'])/TKmM);
            revisionKm = (float(fixedcosts_serializer.data['technicalReviews'])/TKmM)
            billsKm = (float(generaldata_serializer.data['adminexpensesmonth'])/loadVehicle)/TKmM
            servicesKm = (float(generaldata_serializer.data['basicservicesmonth'])/loadVehicle)/TKmM
            costsKm = (float(fixedcosts_serializer.data['financialCosts'])/TKmM);
            depreciationsKm = ((float(generaldata_serializer.data['vehiclevalue'])*0.1)/12)/TKmM
            permissionsKm = (float(generaldata_serializer.data['permitsqualifications'])/12)/TKmM
            gpsKm = (float(fixedcosts_serializer.data['satelliteTracking'])/TKmM);
            policiesKm = (float(fixedcosts_serializer.data['andeanPolicy'])/TKmM);
            total = salaryKm + garageKm + registrationKm + sureKm + revisionKm + billsKm + servicesKm + costsKm + depreciationsKm + permissionsKm + gpsKm + policiesKm
            fixedc = {
                'salaryA': round((travelsalary*12),2),
                'salary': round(travelsalary),
                'salaryKm': round((travelsalary/TKmM),5),
                'garageA':  round((float(generaldata_serializer.data['garage'])*12),2),
                'garage': float(generaldata_serializer.data['garage']),
                'garageKm': round(garageKm,5),
                'registrationA': float(fixedcosts_serializer.data['vehicleRegistration']),
                'registration': round((float(fixedcosts_serializer.data['vehicleRegistration'])/12),5),
                'registrationKm': round(((float(fixedcosts_serializer.data['vehicleRegistration'])/12)/TKmM),5),
                'sureA': round((float(fixedcosts_serializer.data['insurance'])*12),2),
                'sure': float(fixedcosts_serializer.data['insurance']),
                'sureKm': round((float(fixedcosts_serializer.data['insurance'])/TKmM),5),
                'revisionA': round((float(fixedcosts_serializer.data['technicalReviews'])*12),2),
                'revision':float(fixedcosts_serializer.data['technicalReviews']),
                'revisionKm': round((float(fixedcosts_serializer.data['technicalReviews'])/TKmM),5),
                'billsA': round(((float(generaldata_serializer.data['adminexpensesmonth'])/loadVehicle)*12),2),
                'bills': round((float(generaldata_serializer.data['adminexpensesmonth'])/loadVehicle),2),
                'billsKm': round(((float(generaldata_serializer.data['adminexpensesmonth'])/loadVehicle)/TKmM),5),
                'servicesA': round(((float(generaldata_serializer.data['basicservicesmonth'])/loadVehicle)*12),2),
                'services': round((float(generaldata_serializer.data['basicservicesmonth'])/loadVehicle),2),
                'servicesKm': round(((float(generaldata_serializer.data['basicservicesmonth'])/loadVehicle)/TKmM),5),
                'costsA': round((float(fixedcosts_serializer.data['financialCosts'])*12),2),
                'costs': float(fixedcosts_serializer.data['financialCosts']),
                'costsKm': round((float(fixedcosts_serializer.data['financialCosts'])/TKmM),5),
                'depreciationsA':  round((float(generaldata_serializer.data['vehiclevalue'])*0.1),2),
                'depreciations':  round(((float(generaldata_serializer.data['vehiclevalue'])*0.1)/12),2),
                'depreciationsKm':  round((((float(generaldata_serializer.data['vehiclevalue'])*0.1)/12)/TKmM),5),
                'permissionsA': float(generaldata_serializer.data['permitsqualifications']),
                'permissions':  round((float(generaldata_serializer.data['permitsqualifications'])/12),2),
                'permissionsKm':  round(((float(generaldata_serializer.data['permitsqualifications'])/12)/TKmM), 5),
                'gpsA':  round((float(fixedcosts_serializer.data['satelliteTracking'])*12),2),
                'gps': float(fixedcosts_serializer.data['satelliteTracking']),
                'gpsKm':  round((float(fixedcosts_serializer.data['satelliteTracking'])/TKmM),5),
                'policiesA': round((float(fixedcosts_serializer.data['andeanPolicy'])*12),2),
                'policies': float(fixedcosts_serializer.data['andeanPolicy']),
                'policiesKm':  round((float(fixedcosts_serializer.data['andeanPolicy'])/TKmM),5),
                'total': round(total,2)
            }
            maintenamcecosts = MaintenamceCosts.objects.filter(idvehicle = idvehicle).first()
            maintenamcecosts_serializer = self.maintenamceCosts_serializer_class(maintenamcecosts)
            #tiresAlignment
            num1 = float(maintenamcecosts_serializer.data['fronttiresCkm'])
            num2 = float(maintenamcecosts_serializer.data['drivetiresCkm'])
            num3 = float(maintenamcecosts_serializer.data['dragtiresCkm'])
            num4 = float(maintenamcecosts_serializer.data['wheelsCkm'])
            num5 = float(maintenamcecosts_serializer.data['puncturesanddamageCkm'])
            num6 = float(maintenamcecosts_serializer.data['alignmentCkm'])
            num7 = float(maintenamcecosts_serializer.data['swingingCkm'])
            tiresAlignment = round((num1 + num2 + num3 + num4 + num5 + num6 + num7),5)

            #ordinarymaintenance
            num8 = float(maintenamcecosts_serializer.data['oilchangeCkm'])
            num9 = float(maintenamcecosts_serializer.data['casetransmissionoilCkm'])
            num10 = float(maintenamcecosts_serializer.data['airfiltersCkm'])
            num11 = float(maintenamcecosts_serializer.data['lubricantsfluidsCkm'])
            num12 = float(maintenamcecosts_serializer.data['cleaningCkm'])
            ordinarymaintenance = round((num8 + num9 + num10 + num11 + num12),5)

            #electricsystem
            num13 = float(maintenamcecosts_serializer.data['acCkm'])
            num14 = float(maintenamcecosts_serializer.data['pressuregaugesCkm'])
            num15 = float(maintenamcecosts_serializer.data['glassesandcleaningsystemCkm'])
            num16 = float(maintenamcecosts_serializer.data['lightsCkm'])
            num17 = float(maintenamcecosts_serializer.data['accessoriesCkm'])
            num18 = float(maintenamcecosts_serializer.data['startingmotorCkm'])
            num19 = float(maintenamcecosts_serializer.data['alternatorCkm'])
            num20 = float(maintenamcecosts_serializer.data['batteriesCkm'])
            electricsystem = round((num13 + num14 + num15 + num16 + num17 + num18 + num19 + num20),5)

            #brakingsystem
            num21 = float(maintenamcecosts_serializer.data['minorrepairCkm'])
            num22 = float(maintenamcecosts_serializer.data['majorrepairCkm'])
            num23 = float(maintenamcecosts_serializer.data['adjustmentscalibrationsCkm'])
            num24 = float(maintenamcecosts_serializer.data['drumsCkm'])
            num25 = float(maintenamcecosts_serializer.data['sealsCkm'])
            brakingsystem = round((num21 + num22 + num23 + num24 + num25), 5)

            #suspension
            num26 = float(maintenamcecosts_serializer.data['springsleafspringsCkm'])
            num27 = float(maintenamcecosts_serializer.data['rubberCkm'])
            suspension = round((num26 + num27), 5)

            #transmissionsystem
            num28 = float(maintenamcecosts_serializer.data['addressCkm'])
            num29 = float(maintenamcecosts_serializer.data['pinCkm'])
            num30 = float(maintenamcecosts_serializer.data['clutchclutchCkm'])
            num31 = float(maintenamcecosts_serializer.data['transmissiondifferentialCkm'])
            num32 = float(maintenamcecosts_serializer.data['boxCkm'])
            num33 = float(maintenamcecosts_serializer.data['cardanCkm'])
            num34 = float(maintenamcecosts_serializer.data['frontloadaxleCkm'])
            num35 = float(maintenamcecosts_serializer.data['rearloadaxleCkm'])
            transmissionsystem = round((num28 + num29 + num30 + num31 + num32 + num33 + num34 + num35), 5)

            #enginerepair
            num36 = float(maintenamcecosts_serializer.data['waterpumpCkm'])
            num37 = float(maintenamcecosts_serializer.data['airpurifierCkm'])
            num38 = float(maintenamcecosts_serializer.data['radiatorCkm'])
            num39 = float(maintenamcecosts_serializer.data['intonationtuningCkm'])
            num40 = float(maintenamcecosts_serializer.data['engineoverhaulCkm'])
            num41 = float(maintenamcecosts_serializer.data['turboCkm'])
            num42 = float(maintenamcecosts_serializer.data['fuelpumpCkm'])
            num43 = float(maintenamcecosts_serializer.data['oilsystemCkm'])
            num44 = float(maintenamcecosts_serializer.data['coolingCkm'])
            num45 = float(maintenamcecosts_serializer.data['exhaustsystemCkm'])
            num46 = float(maintenamcecosts_serializer.data['electronicsystemCkm'])
            enginerepair = round(( num36 + num37 + num38 + num39 + num40 + num41 + num42 + num43 + num44 + num45 + num46),5)
            maintenamcec = {
              'tirealignmentA': round(((tiresAlignment*TKmM)*12),2),
              'ordinarymaintenanceA': round(((ordinarymaintenance*TKmM)*12),2),
              'electricsystemA': round(((electricsystem*TKmM)*12),2),
              'brakingsystemA': round(((brakingsystem*TKmM)*12),2),
              'suspensionA': round(((suspension*TKmM)*12),2),
              'transmissionsystemA': round(((transmissionsystem*TKmM)*12),2),
              'enginerepairA': round(((enginerepair*TKmM)*12),2),
              'tirealignment': round((tiresAlignment*TKmM),2),
              'ordinarymaintenance': round((ordinarymaintenance*TKmM),2),
              'electricsystem': round((electricsystem*TKmM),2),
              'brakingsystem': round((brakingsystem*TKmM),2),
              'suspension': round((suspension*TKmM),2),
              'transmissionsystem': round((transmissionsystem*TKmM),2),
              'enginerepair': round((enginerepair*TKmM),2),
              'tirealignmentKm': tiresAlignment,
              'ordinarymaintenanceKm': ordinarymaintenance,
              'electricsystemKm': electricsystem,
              'brakingsystemKm': brakingsystem,
              'suspensionKm': suspension,
              'transmissionsystemKm': transmissionsystem,
              'enginerepairKm': enginerepair,
              'total': maintenamcecosts_serializer.data['total'],
            }
            dieselCostv = 0;
            tollCostv = 0;
            viaticCostv = 0;
            weightsScaleCostv = 0;
            loadDownloadCostv = 0;
            caravanCostv = 0;
            for r in respuesta:
              if r['concepts'] == 'DIESEL':
                dieselCostv += r['amount']
              if r['concepts'] == 'PEAJE':
                tollCostv += r['amount']
              if r['concepts'] == 'VIÁTICOS':
                viaticCostv += r['amount']
              if r['concepts'] == 'PESAS Y BALANZA':
                 weightsScaleCostv += r['amount']
              if r['concepts'] == 'CARGUE Y DESCARGUE':
                loadDownloadCostv += r['amount']
              if r['concepts'] == 'CARAVANA':
                caravanCostv += r['amount']
            kmv = (float(travel_serializer.data['kms']) + float(travel_serializer.data['kmsdes']))*2
            n1 = (float(decimal.Decimal(dieselCostv))/kmv)*1
            n2 = (float(decimal.Decimal(tollCostv))/kmv)*10
            n3 = (float(decimal.Decimal(viaticCostv))/kmv)*1
            n4 = (float(decimal.Decimal(weightsScaleCostv))/kmv)*1
            n5 = (float(decimal.Decimal(loadDownloadCostv))/kmv)*14
            n6 = (float(decimal.Decimal(caravanCostv))/kmv)*14
            total2 = n1 + n2 +n3 + n4 +n4 + n5 +n6
            extrac = {
              'dieselCostv': dieselCostv,
              'dieselKmv': kmv,
              'dieselCantv': 1,
              'dieselCostKm': round(n1,5),
              'tollCostv': tollCostv,
              'tollKmv': kmv,
              'tollCantv': 10,
              'tollCostKm': round(n2,5),
              'viaticCostv': viaticCostv,
              'viaticKmv': kmv,
              'viaticCantv': 1,
              'viaticCostKm': round(n3,5),
              'weightsScaleCostv': weightsScaleCostv,
              'weightsScaleKmv': kmv,
              'weightsScaleCantv': 1,
              'weightsScaleCostKm': round(n4, 5),
              'loadDownloadCostv': loadDownloadCostv,
              'loadDownloadKmv': kmv,
              'loadDownloadCantv': 14,
              'loadDownloadCostKm': round(n5, 5),
              'caravanCostv': caravanCostv,
              'caravanKmv': kmv,
              'caravanCantv': 14,
              'caravanCostKm': round(n6, 5),
              'total': round(total2,2)
            }
            datavehicle = {
              'Vehicle':  vehicle_serializer.data['tuition'],
              'vehicle_use': vehicle_serializer.data['vehicle_use'],
              'employee': vehicle_serializer.data['employee'],
              'Trailer': trailer_serializer.data['tuition'],
              'origen': o,
              'destinations': d,
              'client': c,
              'kms': travel_serializer.data['kms'],
              'kmsdes': travel_serializer.data['kmsdes'],
              'datestart': travel_serializer.data['datestart'],
              'dateend': travel_serializer.data['dateend'],
              'hours': travel_serializer.data['hours'],
              'subtotal': travel_serializer.data['subtotal'],
              'percentage': travel_serializer.data['percentage'],
              'total': travel_serializer.data['total'],
              'profitability': travel_serializer.data['profitability'],
              'fixedcost': fixedc,
              'maintenamcecost': maintenamcec,
              'extracost': extrac
            }
            return Response(datavehicle, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

class ReportReceptionPdf(generics.ListAPIView):
      serializer_class = TravelSerializer
      list_serializer_class = TravelListSerializer
      vehicle_serializer_class = VehicleListSerializer
      trailer_serializer_class = TrailerListSerializer
      guide_list_serializer_class = GuideListSerializer
      guide_serializer_class = GuideSerializer
      generaldata_serializer_class = GeneralDataSerializer
      employee_serializer_class = EmployeeSerializer
      fixedcosts_serializer_class = FixedCostsSerializer
      company_serializer_class = CompanySerializer
      maintenamceCosts_serializer_class = MaintenamceCostsSerializer
      bill_serializer_class = BillListSerializer
      tabulation_serializer_class = TabulationListSerializer

      def get_queryset(self):
            return Travel.objects.all()

      def list(self, request, pk= None, idcompany= None):
            travel = Travel.objects.filter(idtravel = pk).first()
            suma = 0
            if(travel):
                  result = []
                  location = []
                  destinations = []
                  client = []
                  respuesta = []
                  travel_serializer = self.serializer_class(travel)
                  idvehicle = travel_serializer.data['idvehicle']
                  idtrailer = travel_serializer.data['idtrailer']
                  vehicle = Vehicle.objects.filter( idvehicle= idvehicle).first()
                  vehicle_serializer =  self.vehicle_serializer_class(vehicle)
                  trailer = Trailer.objects.filter(idtrailer=idtrailer).first()
                  trailer_serializer = self.trailer_serializer_class(trailer)
                  guidedata = travel_serializer.data['guide']
                  for i in guidedata:
                        guide =  Guide.objects.filter(idguide = i).first()
                        guide_list_serialize = self.guide_list_serializer_class(guide)
                        guide_serialize = self.guide_serializer_class(guide)
                        idlocation = guide_serialize.data['idlocation']
                        iddestinations = guide_serialize.data['iddestinations']
                        tabulation = Tabulation.objects.filter(idcompany = idcompany, idlocation= idlocation, iddestinations=iddestinations).first()
                        serializer_tabulation = self.tabulation_serializer_class(tabulation)
                        tabulationresult = serializer_tabulation.data
                        idtabulation = tabulationresult['idtabulation']
                        bill = Bill.objects.filter(idcompany = idcompany, idtabulation = idtabulation)
                        bill_serializer = self.bill_serializer_class(bill, many = True)
                        for i1 in bill_serializer.data:
                          respuesta.append(i1)
                          suma += i1['amount']
                        result.append({
                            'datestart': travel_serializer.data['datestart'],
                            'guia': i,
                            'rute': guide_list_serialize.data['location'] +' / ' + guide_list_serialize.data['destinations'],
                            'vehicle_use': vehicle_serializer.data['vehicle_use'],
                            'location': guide_list_serialize.data['location'],
                            'client': guide_list_serialize.data['client'],
                            'bill': bill_serializer.data,
                            'totalbill': suma,
                            'Vehicle':  vehicle_serializer.data['tuition'],
                            'employee': vehicle_serializer.data['employee'],
                            'Trailer': trailer_serializer.data['tuition'],
                            'destinations': guide_list_serialize.data['destinations'],
                            'dateend': travel_serializer.data['dateend'],
                            'hours':  travel_serializer.data['dateend']
                          })
                        suma = 0
                        location.append(guide_list_serialize.data['location'])
                        destinations.append(guide_list_serialize.data['destinations'])
                        client.append(guide_list_serialize.data['client'])
                  return Response( result, status=status.HTTP_200_OK)
            return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)
