from django.db import models
from simple_history.models import HistoricalRecords
from apps.company.models import Company
from apps.employees.models import Employee

class Owner(models.Model):
    idowner = models.AutoField(db_column='IdOwner', primary_key=True)
    name = models.CharField(db_column='Name', max_length=250,null=False,blank=False)
    idcompany = models.ForeignKey(Company,on_delete=models.CASCADE,db_column='IdCompany')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Owner'

    def __str__(self) -> str:
        return self.name

class VehicleUse(models.Model):
    idvehicle_use = models.AutoField(db_column='IdVehicleUse', primary_key=True)
    vehicle_use = models.CharField(db_column='VehicleUse', max_length=255,null=False,blank=False)
    category = models.CharField(db_column='Category', max_length=255,null=False,blank=False)
    apply_in = models.CharField(db_column='ApplyIn', max_length=255,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'UseVehicle'

    def __str__(self) -> str:
        return self.vehicle_use

class Axes(models.Model):
    idaxis = models.AutoField(db_column='IdAxis', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255,null=False,blank=False)
    number_axes = models.CharField(db_column='Numberaxes', max_length=255,null=False,blank=False)
    diagram = models.ImageField(db_column='Diagram', upload_to='diagram/', max_length=255, null=True, blank = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Axes'

    def __str__(self) -> str:
        return self.name

class Manufacturer(models.Model):
    idmanufacturer = models.AutoField(db_column='IdManufacturer', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255,null=False,blank=False)
    model_types = models.CharField(db_column='Model_types', max_length=255,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Manufacturer'

    def __str__(self) -> str:
        return self.name

class VehicleType(models.Model):
    idvehicle_type = models.AutoField(db_column='IdVehicleType', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100,null=False,blank=False)
    depends_other_vehicle = models.BooleanField(db_column='DependsOtherVehicle',default=False,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'VehicleModel'

    def __str__(self) -> str:
        return self.name

class Fuel(models.Model):
    idfuel = models.AutoField(db_column='IdFuel', primary_key=True)
    type_fuel = models.CharField(db_column='TypeFuel', max_length=255,null=False,blank=False)
    #capacity = models.DecimalField(db_column='Capacity', max_digits=10, decimal_places=2,null=False,blank=False)
    performance = models.DecimalField(db_column='Performance', max_digits=10, decimal_places=2,null=True,blank=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Fuel'

    def __str__(self) -> str:
        return self.type_fuel

class VehicleModel(models.Model):
    idvehicle_model = models.AutoField(db_column='IdVehicleModel', primary_key=True)
    idmanufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,db_column='IdManufacturer')
    model = models.CharField(db_column='Model', max_length=255,null=False,blank=False)
    year = models.DateField(db_column='Year',null=False,blank=False)
    idvehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE,db_column='IdVehicleType')
    kind = models.CharField(db_column='Kind', max_length=255,null=False,blank=False)
    idfuel = models.ForeignKey(Fuel, on_delete=models.CASCADE,db_column='IdFuel')
    idaxis = models.ForeignKey(Axes,on_delete=models.CASCADE,db_column='IdAxis')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'VehicleModel'

    def __str__(self) -> str:
        return self.model

class TechnicalData(models.Model):
    idtechnical_data = models.AutoField(db_column='IdTechnicalData', primary_key=True)
    load_capacity = models.IntegerField(db_column='LoadCapacity',null=False,blank=False)
    color = models.CharField(db_column='Color', max_length=255,null=False,blank=False)
    mileage = models.IntegerField(db_column='Mileage',null=False,blank=False)
    hours_use = models.IntegerField(db_column='HoursUse',null=True,blank=True)
    tank_capacity =  models.IntegerField(db_column='TankCapacity',null=True,blank=True)
    yield_gallon = models.DecimalField(db_column='YieldGallon', decimal_places=2, max_digits=10,null=True,blank=True)
    observation = models.CharField(db_column='Observation', max_length=255, null=True,blank=True)
    idfuel = models.ForeignKey(Fuel,on_delete=models.CASCADE,db_column='IdFuel')
    year = models.CharField(db_column='Year', max_length=4, null=True, blank=True)
    idgps = models.IntegerField(db_column='IdGps',null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'TechnicalData'

    def __str__(self) -> str:
        return self.color

class Vehicle(models.Model):
    idvehicle = models.AutoField(db_column='IdVehicle', primary_key=True)
    #license_plate = models.CharField(db_column='LicensePlate', max_length=100,unique=True,null=True,blank=True)
    idowner = models.ForeignKey(Owner,on_delete=models.CASCADE,db_column='IdOwner')
    idvehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE,db_column='IdVehicleModel')
    idemployee = models.ForeignKey(Employee,on_delete=models.CASCADE, db_column='IdEmployee')
    idvehicle_use = models.ForeignKey(VehicleUse,on_delete=models.CASCADE,db_column='IdVehicleUse')
    agination_date = models.DateField(db_column='aginationDate')
    image = models.ImageField(db_column='Image', upload_to='vehicle/', max_length=255,null=True,blank=True)
    tuition = models.CharField(db_column='Tuition', max_length=100,unique=True,null=False,blank=False) #matricula
    engine_series = models.CharField(db_column='EngineSeries', max_length=100,null=False,blank=False)
    state = models.BooleanField(db_column='State', default= True)
    create_date = models.DateField(db_column='CreateData',auto_now=True,auto_now_add=False)
    idtechnical_data = models.ForeignKey(TechnicalData, on_delete=models.CASCADE,db_column='IdTechnicalData')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Vehicle'

    def __str__(self) -> str:
        return self.tuition

class TechnicalDataTrailer(models.Model):
    idtechnical_datatrailer = models.AutoField(db_column='IdTechnicalDataTrailer', primary_key=True)
    load_capacity = models.IntegerField(db_column='LoadCapacity',null=False,blank=False)
    color = models.CharField(db_column='Color', max_length=255,null=False,blank=False)
    hours_use = models.IntegerField(db_column='HoursUse',null=True,blank=True)
    observation = models.CharField(db_column='Observation', max_length=255,null=True,blank=True)
    idadministrative_data = models.IntegerField(db_column='IdAdministrativeData',null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'TechnicalData'

    def __str__(self) -> str:
        return self.color

class Trailer(models.Model):
    idtrailer = models.AutoField(db_column='IdTrailer', primary_key=True)
    idowner = models.ForeignKey(Owner,on_delete=models.CASCADE,db_column='IdOwner')
    idvehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE,db_column='IdVehicleModel')
    idvehicle_use = models.ForeignKey(VehicleUse,on_delete=models.CASCADE,db_column='IdVehicleUse')
    image = models.ImageField(db_column='Image', upload_to='vehicle/', max_length=255,null=True,blank=True)
    tuition = models.CharField(db_column='Tuition', max_length=100,unique=True,null=False,blank=False) #matricula
    state = models.BooleanField(db_column='State', default= True)
    create_date = models.DateField(db_column='CreateData',auto_now=True,auto_now_add=False)
    idtechnical_datatrailer = models.ForeignKey(TechnicalDataTrailer, on_delete=models.CASCADE,db_column='IdTechnicalDataTrailer')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Trailer'

    def __str__(self) -> str:
        return self.tuition

class GeneralData(models.Model):
    idgeneraldata = models.AutoField(db_column='IdGeneralData', primary_key=True)
    adminexpensesmonth = models.DecimalField(db_column='AdminExpensesMonth', decimal_places=2, max_digits=10, null=False,blank=False)
    basicservicesmonth = models.DecimalField(db_column='BasicServicesMonth', decimal_places=2, max_digits=10, null=False,blank=False)
    garage = models.DecimalField(db_column='Garage', decimal_places=2, max_digits=10, null=False,blank=False)
    nkmmonth = models.DecimalField(db_column='NkmMonth', decimal_places=2, max_digits=10, null=False,blank=False)
    ntravelkmmonth = models.DecimalField(db_column='NtravelKmMonth', decimal_places=2, max_digits=10, null=False,blank=False)
    permitsqualifications = models.DecimalField(db_column='PermitsQualifications', decimal_places=2, max_digits=10, null=False,blank=False)
    vehiclevalue = models.DecimalField(db_column='VehicleValue', decimal_places=2, max_digits=10, null=False,blank=False)
    idvehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,db_column='IdVehicle')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'GeneralData'

    def __str__(self) -> str:
        return 'idgeneralData: {}'.format(self.idgeneraldata)

class MaintenamceCosts(models.Model):
    idmaintenamceCosts= models.AutoField(db_column='IdMaintenamceCosts', primary_key=True)
    acCu =  models.DecimalField(db_column='AcCu', decimal_places=2, max_digits=15, null=True,blank=True)
    acDkm =  models.IntegerField(db_column='AcDkm', null=True,blank=True)
    acQ =  models.IntegerField(db_column='AcQ', null=True,blank=True)
    acCkm = models.DecimalField(db_column='AcCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    accessoriesCkm =  models.DecimalField(db_column='AccessoriesCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    accessoriesCu =  models.DecimalField(db_column='AccessoriesCu', decimal_places=2, max_digits=15, null=True,blank=True)
    accessoriesDkm =  models.IntegerField(db_column='AccessoriesDkm', null=True,blank=True)
    accessoriesQ =  models.IntegerField(db_column='AccessoriesQ', null=True,blank=True)
    addressCkm =  models.DecimalField(db_column='AddressCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    addressCu =  models.DecimalField(db_column='AddressCu', decimal_places=2, max_digits=15, null=True,blank=True)
    addressDkm =  models.IntegerField(db_column='AddressDkm', null=True,blank=True)
    addressQ =  models.IntegerField(db_column='AddressQ', null=True,blank=True)
    adjustmentscalibrationsCkm =  models.DecimalField(db_column='AdjustmentscalibrationsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    adjustmentscalibrationsCu =  models.DecimalField(db_column='AdjustmentscalibrationsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    adjustmentscalibrationsDkm =  models.IntegerField(db_column='AdjustmentscalibrationsDkm', null=True,blank=True)
    adjustmentscalibrationsQ =  models.IntegerField(db_column='AdjustmentscalibrationsQ', null=True,blank=True)
    airfiltersCkm =  models.DecimalField(db_column='AirfiltersCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    airfiltersCu =  models.DecimalField(db_column='AirfiltersCu', decimal_places=2, max_digits=15, null=True,blank=True)
    airfiltersDkm =  models.IntegerField(db_column='AirfiltersDkm', null=True,blank=True)
    airfiltersQ =  models.IntegerField(db_column='AirfiltersQ', null=True,blank=True)
    airpurifierCkm =  models.DecimalField(db_column='AirpurifierCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    airpurifierCu =  models.DecimalField(db_column='AirpurifierCu', decimal_places=2, max_digits=15, null=True,blank=True)
    airpurifierDkm =  models.IntegerField(db_column='AirpurifierDkm', null=True,blank=True)
    airpurifierQ =  models.IntegerField(db_column='AirpurifierQ', null=True,blank=True)
    alignmentCkm =  models.DecimalField(db_column='AlignmentCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    alignmentCu =  models.DecimalField(db_column='AlignmentCu', decimal_places=2, max_digits=15, null=True,blank=True)
    alignmentDkm =  models.IntegerField(db_column='AlignmentDkm', null=True,blank=True)
    alignmentQ =  models.IntegerField(db_column='AlignmentQ', null=True,blank=True)
    alternatorCkm =  models.DecimalField(db_column='AlternatorCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    alternatorCu =  models.DecimalField(db_column='AlternatorCu', decimal_places=2, max_digits=15, null=True,blank=True)
    alternatorDkm =  models.IntegerField(db_column='AlternatorDkm', null=True,blank=True)
    alternatorQ =  models.IntegerField(db_column='AlternatorQ', null=True,blank=True)
    batteriesCkm =  models.DecimalField(db_column='BatteriesCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    batteriesCu =  models.DecimalField(db_column='BatteriesCu', decimal_places=2, max_digits=15, null=True,blank=True)
    batteriesDkm =  models.IntegerField(db_column='BatteriesDkm', null=True,blank=True)
    batteriesQ =  models.IntegerField(db_column='BatteriesQ', null=True,blank=True)
    boxCkm =  models.DecimalField(db_column='BoxCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    boxCu =  models.DecimalField(db_column='BoxCu', decimal_places=2, max_digits=15, null=True,blank=True)
    boxDkm =  models.IntegerField(db_column='BoxDkm', null=True,blank=True)
    boxQ =  models.IntegerField(db_column='BoxQ', null=True,blank=True)
    cardanCkm =  models.DecimalField(db_column='CardanCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    cardanCu =  models.DecimalField(db_column='CardanCu', decimal_places=2, max_digits=15, null=True,blank=True)
    cardanDkm =  models.IntegerField(db_column='CardanDkm', null=True,blank=True)
    cardanQ =  models.IntegerField(db_column='CardanQ', null=True,blank=True)
    casetransmissionoilCkm =  models.DecimalField(db_column='CasetransmissionoilCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    casetransmissionoilCu =  models.DecimalField(db_column='CasetransmissionoilCu', decimal_places=2, max_digits=15, null=True,blank=True)
    casetransmissionoilDkm =  models.IntegerField(db_column='CasetransmissionoilDkm', null=True,blank=True)
    casetransmissionoilQ =  models.IntegerField(db_column='CasetransmissionoilQ', null=True,blank=True)
    cleaningCkm =  models.DecimalField(db_column='CleaningCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    cleaningCu =  models.DecimalField(db_column='CleaningCu', decimal_places=2, max_digits=15, null=True,blank=True)
    cleaningDkm =  models.IntegerField(db_column='CleaningDkm', null=True,blank=True)
    cleaningQ =  models.IntegerField(db_column='CleaningQ', null=True,blank=True)
    clutchclutchCkm =  models.DecimalField(db_column='ClutchclutchCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    clutchclutchCu =  models.DecimalField(db_column='ClutchclutchCu', decimal_places=2, max_digits=15, null=True,blank=True)
    clutchclutchDkm =  models.IntegerField(db_column='ClutchclutchDkm', null=True,blank=True)
    clutchclutchQ =  models.IntegerField(db_column='ClutchclutchQ', null=True,blank=True)
    coolingCkm =  models.DecimalField(db_column='CoolingCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    coolingCu =  models.DecimalField(db_column='CoolingCu', decimal_places=2, max_digits=15, null=True,blank=True)
    coolingDkm =  models.IntegerField(db_column='CoolingDkm', null=True,blank=True)
    coolingQ =  models.IntegerField(db_column='CoolingQ', null=True,blank=True)
    dragtiresCkm =  models.DecimalField(db_column='DragtiresCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    dragtiresCu =  models.DecimalField(db_column='DragtiresCu', decimal_places=2, max_digits=15, null=True,blank=True)
    dragtiresDkm =  models.IntegerField(db_column='DragtiresDkm', null=True,blank=True)
    dragtiresQ =  models.IntegerField(db_column='DragtiresQ', null=True,blank=True)
    drivetiresCkm =  models.DecimalField(db_column='DrivetiresCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    drivetiresCu =  models.DecimalField(db_column='DrivetiresCu', decimal_places=2, max_digits=15, null=True,blank=True)
    drivetiresDkm =  models.IntegerField(db_column='DrivetiresDkm', null=True,blank=True)
    drivetiresQ =  models.IntegerField(db_column='DrivetiresQ', null=True,blank=True)
    drumsCkm =  models.DecimalField(db_column='DrumsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    drumsCu =  models.DecimalField(db_column='DrumsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    drumsDkm =  models.IntegerField(db_column='DrumsDkm', null=True,blank=True)
    drumsQ =  models.IntegerField(db_column='DrumsQ', null=True,blank=True)
    electronicsystemCkm =  models.DecimalField(db_column='ElectronicsystemCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    electronicsystemCu =  models.DecimalField(db_column='ElectronicsystemCu', decimal_places=2, max_digits=15, null=True,blank=True)
    electronicsystemDkm =  models.IntegerField(db_column='ElectronicsystemDkm', null=True,blank=True)
    electronicsystemQ =  models.IntegerField(db_column='ElectronicsystemQ', null=True,blank=True)
    engineoverhaulCkm =  models.DecimalField(db_column='EngineoverhaulCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    engineoverhaulCu =  models.DecimalField(db_column='EngineoverhaulCu', decimal_places=2, max_digits=15, null=True,blank=True)
    engineoverhaulDkm =  models.IntegerField(db_column='EngineoverhaulDkm', null=True,blank=True)
    engineoverhaulQ =  models.IntegerField(db_column='EngineoverhaulQ', null=True,blank=True)
    exhaustsystemCkm =  models.DecimalField(db_column='ExhaustsystemCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    exhaustsystemCu =  models.DecimalField(db_column='ExhaustsystemCu', decimal_places=2, max_digits=15, null=True,blank=True)
    exhaustsystemDkm =  models.IntegerField(db_column='ExhaustsystemDkm', null=True,blank=True)
    exhaustsystemQ =  models.IntegerField(db_column='ExhaustsystemQ', null=True,blank=True)
    frontloadaxleCkm =  models.DecimalField(db_column='FrontloadaxleCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    frontloadaxleCu =  models.DecimalField(db_column='FrontloadaxleCu', decimal_places=2, max_digits=15, null=True,blank=True)
    frontloadaxleDkm =  models.IntegerField(db_column='FrontloadaxleDkm', null=True,blank=True)
    frontloadaxleQ =  models.IntegerField(db_column='FrontloadaxleQ', null=True,blank=True)
    fronttiresCkm =  models.DecimalField(db_column='FronttiresCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    fronttiresCu =  models.DecimalField(db_column='FronttiresCu', decimal_places=2, max_digits=15, null=True,blank=True)
    fronttiresDkm =  models.IntegerField(db_column='FronttiresDkm', null=True,blank=True)
    fronttiresQ =  models.IntegerField(db_column='FronttiresQ', null=True,blank=True)
    fuelpumpCkm =  models.DecimalField(db_column='FuelpumpCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    fuelpumpCu =  models.DecimalField(db_column='FuelpumpCu', decimal_places=2, max_digits=15, null=True,blank=True)
    fuelpumpDkm =  models.IntegerField(db_column='FuelpumpDkm', null=True,blank=True)
    fuelpumpQ =  models.IntegerField(db_column='FuelpumpQ', null=True,blank=True)
    glassesandcleaningsystemCkm =  models.DecimalField(db_column='GlassesandcleaningsystemCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    glassesandcleaningsystemCu =  models.DecimalField(db_column='GlassesandcleaningsystemCu', decimal_places=2, max_digits=15, null=True,blank=True)
    glassesandcleaningsystemDkm =  models.IntegerField(db_column='GlassesandcleaningsystemDkm', null=True,blank=True)
    glassesandcleaningsystemQ =  models.IntegerField(db_column='GlassesandcleaningsystemQ', null=True,blank=True)
    idvehicle =  models.DecimalField(db_column='Idvehicle', decimal_places=5, max_digits=15, null=True,blank=True)
    intonationtuningCkm =  models.DecimalField(db_column='IntonationtuningCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    intonationtuningCu =  models.DecimalField(db_column='IntonationtuningCu', decimal_places=2, max_digits=15, null=True,blank=True)
    intonationtuningDkm =  models.IntegerField(db_column='IntonationtuningDkm', null=True,blank=True)
    intonationtuningQ =  models.IntegerField(db_column='IntonationtuningQ', null=True,blank=True)
    lightsCkm =  models.DecimalField(db_column='LightsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    lightsCu =  models.DecimalField(db_column='LightsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    lightsDkm =  models.IntegerField(db_column='LightsDkm', null=True,blank=True)
    lightsQ =  models.IntegerField(db_column='LightsQ', null=True,blank=True)
    lubricantsfluidsCkm =  models.DecimalField(db_column='LubricantsfluidsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    lubricantsfluidsCu =  models.DecimalField(db_column='LubricantsfluidsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    lubricantsfluidsDkm =  models.IntegerField(db_column='LubricantsfluidsDkm', null=True,blank=True)
    lubricantsfluidsQ =  models.IntegerField(db_column='LubricantsfluidsQ', null=True,blank=True)
    majorrepairCkm =  models.DecimalField(db_column='MajorrepairCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    majorrepairCu =  models.DecimalField(db_column='MajorrepairCu', decimal_places=2, max_digits=15, null=True,blank=True)
    majorrepairDkm =  models.IntegerField(db_column='MajorrepairDkm', null=True,blank=True)
    majorrepairQ =  models.IntegerField(db_column='MajorrepairQ', null=True,blank=True)
    minorrepairCkm =  models.DecimalField(db_column='MinorrepairCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    minorrepairCu =  models.DecimalField(db_column='MinorrepairCu', decimal_places=2, max_digits=15, null=True,blank=True)
    minorrepairDkm =  models.IntegerField(db_column='MinorrepairDkm', null=True,blank=True)
    minorrepairQ =  models.IntegerField(db_column='MinorrepairQ', null=True,blank=True)
    oilchangeCkm =  models.DecimalField(db_column='OilchangeCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    oilchangeCu =  models.DecimalField(db_column='OilchangeCu', decimal_places=2, max_digits=15, null=True,blank=True)
    oilchangeDkm =  models.IntegerField(db_column='OilchangeDkm', null=True,blank=True)
    oilchangeQ =  models.IntegerField(db_column='OilchangeQ', null=True,blank=True)
    oilsystemCkm =  models.DecimalField(db_column='OilsystemCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    oilsystemCu =  models.DecimalField(db_column='OilsystemCu', decimal_places=2, max_digits=15, null=True,blank=True)
    oilsystemDkm =  models.IntegerField(db_column='OilsystemDkm', null=True,blank=True)
    oilsystemQ =  models.IntegerField(db_column='OilsystemQ', null=True,blank=True)
    pinCkm =  models.DecimalField(db_column='PinCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    pinCu =  models.DecimalField(db_column='PinCu', decimal_places=2, max_digits=15, null=True,blank=True)
    pinDkm =  models.IntegerField(db_column='PinDkm', null=True,blank=True)
    pinQ =  models.IntegerField(db_column='PinQ', null=True,blank=True)
    pressuregaugesCkm =  models.DecimalField(db_column='PressuregaugesCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    pressuregaugesCu =  models.DecimalField(db_column='PressuregaugesCu', decimal_places=2, max_digits=15, null=True,blank=True)
    pressuregaugesDkm =  models.IntegerField(db_column='PressuregaugesDkm', null=True,blank=True)
    pressuregaugesQ =  models.IntegerField(db_column='PressuregaugesQ', null=True,blank=True)
    puncturesanddamageCkm =  models.DecimalField(db_column='PuncturesanddamageCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    puncturesanddamageCu =  models.DecimalField(db_column='PuncturesanddamageCu', decimal_places=2, max_digits=15, null=True,blank=True)
    puncturesanddamageDkm =  models.IntegerField(db_column='PuncturesanddamageDkm', null=True,blank=True)
    puncturesanddamageQ =  models.IntegerField(db_column='PuncturesanddamageQ', null=True,blank=True)
    radiatorCkm =  models.DecimalField(db_column='RadiatorCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    radiatorCu =  models.DecimalField(db_column='RadiatorCu', decimal_places=2, max_digits=15, null=True,blank=True)
    radiatorDkm =  models.IntegerField(db_column='RadiatorDkm', null=True,blank=True)
    radiatorQ =  models.IntegerField(db_column='RadiatorQ', null=True,blank=True)
    rearloadaxleCkm =  models.DecimalField(db_column='RearloadaxleCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    rearloadaxleCu =  models.DecimalField(db_column='RearloadaxleCu', decimal_places=2, max_digits=15, null=True,blank=True)
    rearloadaxleDkm =  models.IntegerField(db_column='RearloadaxleDkm', null=True,blank=True)
    rearloadaxleQ =  models.IntegerField(db_column='RearloadaxleQ', null=True,blank=True)
    rubberCkm =  models.DecimalField(db_column='RubberCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    rubberCu =  models.DecimalField(db_column='RubberCu', decimal_places=2, max_digits=15, null=True,blank=True)
    rubberDkm =  models.IntegerField(db_column='RubberDkm', null=True,blank=True)
    rubberQ =  models.IntegerField(db_column='RubberQ', null=True,blank=True)
    sealsCkm =  models.DecimalField(db_column='SealsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    sealsCu =  models.DecimalField(db_column='SealsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    sealsDkm =  models.IntegerField(db_column='SealsDkm', null=True,blank=True)
    sealsQ =  models.IntegerField(db_column='SealsQ', null=True,blank=True)
    springsleafspringsCkm =  models.DecimalField(db_column='SpringsleafspringsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    springsleafspringsCu =  models.DecimalField(db_column='SpringsleafspringsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    springsleafspringsDkm =  models.IntegerField(db_column='SpringsleafspringsDkm', null=True,blank=True)
    springsleafspringsQ =  models.IntegerField(db_column='SpringsleafspringsQ', null=True,blank=True)
    startingmotorCkm =  models.DecimalField(db_column='StartingmotorCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    startingmotorCu =  models.DecimalField(db_column='StartingmotorCu', decimal_places=2, max_digits=15, null=True,blank=True)
    startingmotorDkm =  models.IntegerField(db_column='StartingmotorDkm', null=True,blank=True)
    startingmotorQ =  models.IntegerField(db_column='StartingmotorQ', null=True,blank=True)
    swingingCkm =  models.DecimalField(db_column='SwingingCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    swingingCu =  models.DecimalField(db_column='SwingingCu', decimal_places=2, max_digits=15, null=True,blank=True)
    swingingDkm =  models.IntegerField(db_column='SwingingDkm', null=True,blank=True)
    swingingQ =  models.IntegerField(db_column='SwingingQ', null=True,blank=True)
    total =  models.DecimalField(db_column='Total', decimal_places=2, max_digits=15, null=True,blank=True)
    transmissiondifferentialCkm =  models.DecimalField(db_column='TransmissiondifferentialCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    transmissiondifferentialCu =  models.DecimalField(db_column='TransmissiondifferentialCu', decimal_places=2, max_digits=15, null=True,blank=True)
    transmissiondifferentialDkm =  models.IntegerField(db_column='TransmissiondifferentialDkm', null=True,blank=True)
    transmissiondifferentialQ =  models.IntegerField(db_column='TransmissiondifferentialQ', null=True,blank=True)
    turboCkm =  models.DecimalField(db_column='TurboCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    turboCu =  models.DecimalField(db_column='TurboCu', decimal_places=2, max_digits=15, null=True,blank=True)
    turboDkm =  models.IntegerField(db_column='TurboDkm', null=True,blank=True)
    turboQ =  models.IntegerField(db_column='TurboQ', null=True,blank=True)
    waterpumpCkm =  models.DecimalField(db_column='WaterpumpCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    waterpumpCu =  models.DecimalField(db_column='WaterpumpCu', decimal_places=2, max_digits=15, null=True,blank=True)
    waterpumpDkm =  models.IntegerField(db_column='WaterpumpDkm', null=True,blank=True)
    waterpumpQ =  models.IntegerField(db_column='WaterpumpQ', null=True,blank=True)
    wheelsCkm =  models.DecimalField(db_column='WheelsCkm', decimal_places=5, max_digits=15, null=True,blank=True)
    wheelsCu =  models.DecimalField(db_column='WheelsCu', decimal_places=2, max_digits=15, null=True,blank=True)
    wheelsDkm =  models.IntegerField(db_column='WheelsDkm', null=True,blank=True)
    wheelsQ =  models.IntegerField(db_column='WheelsQ', null=True,blank=True)
    idvehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,db_column='IdVehicle')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'MaintenamceCosts'

    def __str__(self) -> str:
        return 'IdMaintenamceCosts: {}'.format(self.idmaintenamceCosts)

class DocumentType(models.Model):
    iddocument_type = models.AutoField(db_column='IdDocumentType',primary_key=True)
    name = models.CharField(db_column='Name',max_length=50,null=False,blank=False)
    description = models.TextField(db_column='Description',null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'DocumentType'

    def __str__(self) -> str:
        return self.name

class DocumentVehicle(models.Model):
    iddocument_vehicle = models.AutoField(db_column='IdDocumentVehicle', primary_key=True)
    iddocument_type = models.ForeignKey(DocumentType,on_delete=models.CASCADE,db_column='IdDocumentType')
    issue_date = models.DateField(db_column='Issue_Date',null=False,blank=False)
    expiration_date = models.DateField(db_column='Expiration_Date',null=False,blank=False)
    attachment = models.FileField(db_column='Attachment',upload_to='document/employee/', max_length=255,null=True,blank=True)
    procedure_cost = models.DecimalField(db_column='ProcedureCosto', max_digits=10, decimal_places=2,null=False,blank=False)
    observations = models.CharField(db_column='Observations', max_length=255,null=False,blank=False)
    idvehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,db_column='IdtVehicle')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'DocumentVehicle'

    def __str__(self) -> str:
        return 'documeto {}'.format(self.iddocument_vehicle)

class AssignTrailer(models.Model):
    idassigntrailer = models.AutoField(db_column='IidAssignTrailer', primary_key=True)
    dateassign = models.DateField(db_column='Issue_Date',null=False,blank=False)
    observations = models.CharField(db_column='Observations', max_length=255,null=True,blank=True)
    idvehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,db_column='IdVehicle')
    idtrailer = models.ForeignKey(Trailer,on_delete=models.CASCADE,db_column='IdTrailer')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'AssignTrailer'

    def __str__(self) -> str:
        return 'AssignTrailer {}'.format(self.idassigntrailer)

class FixedCosts(models.Model):
    idfixedcosts = models.AutoField(db_column='IdFixedCosts', primary_key=True)
    andeanPolicy =  models.DecimalField(db_column='AndeanPolicy', decimal_places=2, max_digits=10, null=False,blank=False)
    financialCosts =  models.DecimalField(db_column='FinancialCosts', decimal_places=2, max_digits=10, null=False,blank=False)
    insurance =  models.DecimalField(db_column='Insurance', decimal_places=2, max_digits=10, null=False, blank=False)
    satelliteTracking =  models.DecimalField(db_column='SatelliteTracking', decimal_places=2, max_digits=10, null=False,blank=False)
    technicalReviews =  models.DecimalField(db_column='TechnicalReviews', decimal_places=2, max_digits=10, null=False, blank=False)
    vehicleRegistration =  models.DecimalField(db_column='VehicleRegistration', decimal_places=2, max_digits=10, null=False, blank=False)
    idvehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,db_column='IdtVehicle')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'FixedCosts'

    def __str__(self) -> str:
        return 'FixedCosts {}'.format(self.idassigntrailer)