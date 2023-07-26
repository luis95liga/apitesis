from django.db import models
from simple_history.models import HistoricalRecords

class Country(models.Model):
    idcountry = models.SmallAutoField(db_column='IdCountry', primary_key=True)
    initials = models.CharField(db_column='Initials', max_length=3,null=False,blank=False)
    name = models.CharField(db_column='Name', max_length=20,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Country'

    def __str__(self) -> str:
        return self.name

class Province(models.Model):
    idprovince = models.AutoField(db_column='IdProvince', primary_key=True)
    idcountry = models.ForeignKey(Country,on_delete=models.CASCADE,db_column='IdCountry')
    name = models.CharField(db_column='Name', max_length=255, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Province'

    def __str__(self) -> str:
        return self.name

class Locality(models.Model):
    idlocation = models.AutoField(db_column='IdLocation', primary_key=True)
    location = models.CharField(db_column='Location',max_length=250, null=False,blank=False)
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
        db_table = 'Locality'

    def __str__(self) -> str:
        return self.location

class TypeCompany(models.Model):
    idtype_company = models.AutoField(db_column='IdTypeCompany', primary_key=True)
    name = models.CharField(db_column='Name',max_length=100,null=False,blank=False)
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
        db_table = 'Companytype'

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    idcompany = models.AutoField(db_column='IdCompany', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255,null=False,blank=False)
    idtype_company = models.ForeignKey(TypeCompany,on_delete=models.CASCADE,db_column='IdTypeCompany')
    logo = models.ImageField(db_column='Logo', upload_to='logo/', max_length=255, null=True, blank = True)
    ruc = models.CharField(db_column='Ruc',max_length=13,null=False,blank=False)
    idlocation = models.ForeignKey(Locality,on_delete=models.CASCADE,db_column='IdLocation')
    address = models.CharField(db_column='Address', max_length=255,null=False,blank=False)
    email = models.CharField(db_column='Email', max_length=255,null=False,blank=False)
    phone = models.CharField(db_column='Phone', max_length=13,null=False,blank=False)
    tel_atcn_client = models.CharField(db_column='TelAtcnclient', max_length=13,null=False,blank=False)
    cell = models.CharField(db_column='Cell', max_length=13)
    default_load_type = models.IntegerField(db_column='Defaultloadtype',null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value


    class Target:
        managed = False
        db_table = 'Company'

    def __str__(self) -> str:
        return self.name

class BankAccounts(models.Model):
    idbank_account = models.AutoField(db_column='IdBankAccount', primary_key=True)
    bank_name = models.CharField(db_column='BankName', max_length=100,null=False,blank=False)
    account_number = models.CharField(db_column='AccountNumber', max_length=255,null=False,blank=False)
    default = models.BooleanField(db_column='Default ',default=False,null=False,blank=False)
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
        db_table = 'BankAccounts'

    def __str__(self) -> str:
        return self.bank_name

class DocumentType(models.Model):
    iddocument_type = models.AutoField(db_column='IdDocumentType',primary_key=True)
    name = models.CharField(db_column='IdTypeDocument',max_length=100,null=False,blank=False)
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
        db_table = 'DocumentsType'

    def __str__(self) -> str:
        return self.name

class Documents(models.Model):
    iddocument = models.AutoField(db_column='IdDocument', primary_key=True)
    idtype_document = models.ForeignKey(DocumentType,on_delete=models.CASCADE)
    issue_date = models.DateField(db_column='IssueDate',null=False,blank=False)
    expiration_date = models.DateField(db_column='ExpirationDate',null=False,blank=False)
    attachment = models.FileField(db_column='Attachment', upload_to='document/company/', max_length=255, null=True, blank = True)
    cost_procedure = models.DecimalField(db_column='CostProcedure', max_digits=10, decimal_places=2,null=False,blank=False)
    observations = models.CharField(db_column='Observations', max_length=255,null=False,blank=False)
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
        db_table = 'Documents'

    def __str__(self) -> str:
        return self.observations