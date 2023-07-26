from django.db import models
from simple_history.models import HistoricalRecords
from apps.company.models import Company, Locality
from apps.routes.models import Destinations
from apps.client.models import Client
from apps.vehicle.models import Vehicle, Trailer
from apps.employees.models import Employee

class Guide(models.Model):
    idguide = models.AutoField(db_column='IdGuide', primary_key=True)
    idclient = models.ForeignKey(Client,on_delete=models.CASCADE,db_column='IdClient')
    idcompany = models.ForeignKey(Company,on_delete=models.CASCADE,db_column='IdCompany')
    idlocation = models.ForeignKey(Locality,on_delete=models.CASCADE,db_column='IdLocation')
    iddestinations = models.ForeignKey(Destinations,on_delete=models.CASCADE,db_column='IdDestinations')
    km = models.IntegerField(db_column='Km', null=False,blank=False)
    hours = models.IntegerField(db_column='Hours', null=True,blank=True)
    status = models.BooleanField(db_column='State',default=False,null=False,blank=False)
    initialized = models.BooleanField(db_column='initialized',default=False,null=False,blank=False)
    route = models.BooleanField(db_column='Route',default=False,null=False,blank=False)
    finalized  = models.BooleanField(db_column='Finalized',default=False,null=False,blank=False)
    idvehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,db_column='IdVehicle')
    iduser = models.IntegerField(db_column='IdUser', null=True, blank=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Guide'

    def __str__(self) -> str:
        return 'Guide: {} ( {} -> {} )'.format( self.idguide,self.idlocation, self.iddestinations )

class Travel(models.Model):
    idtravel = models.AutoField(db_column='IdTravel', primary_key=True)
    datestart = models.DateField(db_column='DateStart', null= False, blank = False)
    dateend = models.DateField(db_column='DateEnd', null= False, blank = False)
    dif = models.DecimalField(db_column='Dif',  max_digits=10, decimal_places = 2,null= False, blank = False)
    feeding = models.DecimalField(db_column='Feeding',  max_digits=10, decimal_places = 2,null= False, blank = False)
    guide = models.ManyToManyField( Guide, db_column='Guide', related_name='guide', blank = True )
    hours = models.IntegerField(db_column='Hours', null= False,blank = False)
    kms = models.DecimalField(db_column='Kms',  max_digits=10, decimal_places = 2,null= True, blank = True)
    kmsdes = models.IntegerField(db_column='Kmsdes', null= False,blank = False)
    ltes = models.DecimalField(db_column='Ltes',  max_digits=10, decimal_places = 2,null= False, blank = False)
    ltgas  = models.IntegerField(db_column='Ltgas', null= False,blank = False)
    percentage  = models.IntegerField(db_column='Percentage', null= False,blank = False)
    performance = models.DecimalField(db_column='Performance',  max_digits=10, decimal_places = 2,null= False, blank = False)
    profitability = models.DecimalField(db_column='Profitability',  max_digits=10, decimal_places = 2,null= False, blank = False)
    salary = models.DecimalField(db_column='Salary',  max_digits=10, decimal_places = 2,null= False, blank = False)
    subtotal = models.DecimalField(db_column='Subtotal',  max_digits=10, decimal_places = 2,null= False, blank = False)
    tank = models.DecimalField(db_column='Tank',  max_digits=10, decimal_places = 2,null= True, blank = True)
    total = models.DecimalField(db_column='Total',  max_digits=10, decimal_places = 2,null= False, blank = False)
    observations = models.TextField(db_column='Observations', null= False,blank = False)
    idtrailer = models.ForeignKey(Trailer,on_delete=models.CASCADE,db_column='IdTrailer')
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
        db_table = 'Travel'

    def __str__(self) -> str:
        return '{}'.format(self.idtravel)

class InvoiceType(models.Model):
    idinvoicetype = models.AutoField(db_column='IdInvoiceType', primary_key=True)
    invoicetype = models.CharField(db_column='InvoiceType', max_length=225,null= False, blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'InvoiceType'

    def __str__(self) -> str:
        return self.invoicetype

class Unit(models.Model):
    idunit = models.AutoField(db_column='IdUnit', primary_key=True)
    unit = models.CharField(db_column='Unit', max_length=225,null= False, blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Unity'

    def __str__(self) -> str:
        return self.unit

class GuideContent(models.Model):
    idguidecontent = models.AutoField(db_column='IdGuideContent', primary_key=True)
    idguide = models.ForeignKey(Guide , on_delete=models.CASCADE,db_column='IdGuide')
    idinvoicetype = models.ForeignKey(InvoiceType , on_delete=models.CASCADE,db_column='IdInvoiceType')
    authorizacionno = models.CharField(db_column='AuthorizacionNo', max_length=225, null= False, blank = False)
    receiptno = models.CharField(db_column='ReceiptNo', max_length=225, null= False, blank = False)
    customsdeclarationnumber = models.CharField(db_column='CustomsDeclarationNumber', max_length=225, null= True, blank = True)
    reasonfortransfer  = models.CharField(db_column='ReasonForTransfer', max_length=225, null= True, blank = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'GuideContent'

    def __str__(self) -> str:
        return '{}'.format(self.idguidecontent)

class GuideContentDetailTmp(models.Model):
    idguidecontentdetailtmp = models.AutoField(db_column='IdGuideContentDetailTmp', primary_key=True)
    idguide = models.ForeignKey(Guide , on_delete=models.CASCADE,db_column='IdGuide')
    idemployee = models.ForeignKey(Employee, on_delete=models.CASCADE,db_column='IdEmployee')
    description = models.CharField(db_column='Description', max_length=225, null= False, blank = False)
    idunit = models.ForeignKey(Unit, on_delete=models.CASCADE,db_column='IdUnit')
    amount = models.IntegerField(db_column='Amount', null= False, blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'GuideContentDetailTmp'

    def __str__(self) -> str:
        return '{}'.format(self.idguidecontentdetailtpm)

class GuideContentDetail(models.Model):
    idguidecontentdetail = models.AutoField(db_column='IdGuideContentDetail', primary_key=True)
    idguidecontent = models.ForeignKey(GuideContent , on_delete=models.CASCADE,db_column='IdGuideContent')
    description = models.CharField(db_column='Description', max_length=225, null= False, blank = False)
    idunit = models.ForeignKey(Unit, on_delete=models.CASCADE,db_column='IdUnit')
    amount = models.IntegerField(db_column='Amount', null= False, blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'GuideContentDetail'

    def __str__(self) -> str:
        return '{}'.format(self.idguidecontentdetail)