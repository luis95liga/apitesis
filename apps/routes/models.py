from django.db import models
from simple_history.models import HistoricalRecords
from apps.company.models import Company, Province, Locality


class Cellars(models.Model):
    idcellars = models.AutoField(db_column='IdCellars', primary_key=True)
    cellar = models.CharField(db_column='Cellar',max_length=250, null=False,blank=False)
    latitude= models.FloatField(db_column='Latitude', null=True,blank=True)
    longitude= models.FloatField(db_column='Longitude', null=True,blank=True)
    state = models.BooleanField(db_column='State',default=True,null=False,blank=False)
    idprovince = models.ForeignKey(Province,on_delete=models.CASCADE,db_column='IdProvince')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Cellars'

    def __str__(self) -> str:
        return self.cellar


class Destinations(models.Model):
    iddestinations = models.AutoField(db_column='IdDestinations', primary_key=True)
    destinations = models.CharField(db_column='destinations',max_length=250, null=False,blank=False)
    latitude= models.FloatField(db_column='Latitude', null=True,blank=True)
    longitude= models.FloatField(db_column='Longitude', null=True,blank=True)
    state = models.BooleanField(db_column='State',default=True,null=False,blank=False)
    idprovince = models.ForeignKey(Province,on_delete=models.CASCADE,db_column='IdProvince')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Destinations'

    def __str__(self) -> str:
        return self.destinations


class Tabulation(models.Model):
    idtabulation = models.AutoField(db_column='IdTabulation', primary_key=True)
    #idcellars = models.ForeignKey(Cellars,on_delete=models.CASCADE,db_column='IdCellars')
    idlocation = models.ForeignKey(Locality,on_delete=models.CASCADE,db_column='IdLocation')
    iddestinations = models.ForeignKey(Destinations,on_delete=models.CASCADE,db_column='IdDestinations')
    km = models.IntegerField(db_column='Km', null=True,blank=True)
    hours = models.IntegerField(db_column='Hours', null=True,blank=True)
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
        db_table = 'Tabulation'

    def __str__(self) -> str:
        return '{}'.format(self.idtabulation)

class Concepts(models.Model):
    idconcepts = models.AutoField(db_column='IdConcepts', primary_key=True)
    concepts = models.CharField(db_column='Concepts', max_length=60, null= False, blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Concepts'

    def __str__(self) -> str:
        return self.concepts


class Bill(models.Model):
    idbill = models.AutoField(db_column='IdBill', primary_key=True)
    idconcepts = models.ForeignKey( Concepts, on_delete=models.CASCADE, db_column='IdConcepts')
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, null= False, blank= False)
    idtabulation = models.ForeignKey( Tabulation, on_delete=models.CASCADE, db_column='IdTabulation')
    idcompany = models.ForeignKey( Company, on_delete=models.CASCADE, db_column='IdCompany')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Tabulation'

    def __str__(self) -> str:
        return '{}'.format(self.idtabulation)

