from django.db import models
from simple_history.models import HistoricalRecords
from apps.company.models  import Company
from apps.routes.models import Cellars, Destinations

class Client(models.Model):
    idclient = models.AutoField(db_column='IdClient', primary_key=True)
    identificationcard = models.CharField(db_column='IdentificationCard',max_length=10,null=False,blank=False)
    names = models.CharField(db_column='Names', max_length=100)
    lastnames = models.CharField(db_column='Lastname', max_length=100)
    birth_date = models.DateField(db_column='BirthDate')
    photo = models.ImageField(db_column='Photo', upload_to='photo/', max_length=255,null=True,blank=True)
    address = models.CharField(db_column='Address', max_length=255, null=False,blank=False)
    email = models.CharField(db_column='Email', max_length=255, null=False,blank=False)
    phone = models.CharField(db_column='Phone', max_length=255,null=False,blank=False)
    cell = models.CharField(db_column='Cell', max_length=255, null=False,blank=False)
    observations = models.CharField(db_column='Observations', max_length=255,null=True,blank=True)
    iddestinations = models.ForeignKey( Destinations, on_delete=models.CASCADE, db_column='IdDestinations')
    entry_date = models.DateField(db_column='EntryDate',null=False,blank=False)
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
        db_table = 'Client'

    def __str__(self) -> str:
        return 'idclient {}'.format(self.idclient)