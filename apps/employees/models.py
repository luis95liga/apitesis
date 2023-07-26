from django.db import models
from simple_history.models import HistoricalRecords
from apps.company.models  import Locality, Company
from apps.users.models import User

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
        db_table = 'DocumentPerson'

    def __str__(self) -> str:
        return self.name

class PeriodPayment(models.Model):
    idperiod_payment = models.AutoField(db_column='IdPeriodPayment', primary_key=True)
    period = models.CharField(db_column='Period',max_length=100,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'PeriodPayment'

    def __str__(self) -> str:
        return self.period

class PositionType(models.Model):
    idposition_type = models.AutoField(db_column='IdPositionType', primary_key=True)
    job_type_name = models.CharField(db_column='JobTypeName', max_length=255,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'PositionType'


    def __str__(self) -> str:
        return self.job_type_name

class Position(models.Model):
    idposition = models.AutoField(db_column='IdPosition', primary_key=True)
    idposition_type = models.ForeignKey(PositionType,on_delete=models.CASCADE,db_column='IdPositionType')
    job_name = models.CharField(db_column='JobName', max_length=255,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'Charge'

    def __str__(self) -> str:
        return self.job_name

class Employee(models.Model):
    idemployee = models.AutoField(db_column='IdEmployee', primary_key=True)
    identificationcard = models.CharField(db_column='IdentificationCard',max_length=10,null=True,blank=True)
    names = models.CharField(db_column='Names', max_length=100)
    lastnames = models.CharField(db_column='Lastname', max_length=100)
    birth_date = models.DateField(db_column='BirthDate')
    photo = models.ImageField(db_column='Photo', upload_to='photo/', max_length=255,null=True,blank=True)
    address = models.CharField(db_column='Address', max_length=255, null=False,blank=False)
    email = models.CharField(db_column='Email', max_length=255, null=False,blank=False)
    phone = models.CharField(db_column='Phone', max_length=255,null=False,blank=False)
    cell = models.CharField(db_column='Cell', max_length=255, null=False,blank=False)
    observations = models.CharField(db_column='Observations', max_length=255,null=False,blank=False)
    idlocation = models.ForeignKey(Locality,on_delete=models.CASCADE,db_column='IdLocation')
    idposition = models.ForeignKey(Position,on_delete=models.CASCADE,db_column='IdPosition')
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2,null=False,blank=False)
    idperiod_payment = models.ForeignKey(PeriodPayment,on_delete=models.CASCADE,db_column='IdPeriodPayment')
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
        db_table = 'Employee'

    def __str__(self) -> str:
        return 'idemployee {}'.format(self.idemployee)

class LaborPayments(models.Model):
    idlabor_payments = models.AutoField(db_column='IdLaborPayments', primary_key=True)
    payment_type = models.CharField(db_column='PaymentType', max_length=255, null=False,blank=False)
    calculation = models.CharField(db_column='Calculation', max_length=255, null=False,blank=False)
    affects = models.CharField(db_column='Affects', max_length=255, null=False,blank=False)
    idemployee = models.ForeignKey(Employee,on_delete=models.CASCADE, db_column='IdEmployee')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'LaborPayments'

    def __str__(self) -> str:
        return self.payment_type

class IsLogin(models.Model):
    idislogin = models.AutoField(db_column='IdIsLogin', primary_key=True)
    idemployee = models.OneToOneField(Employee,on_delete=models.CASCADE,db_column='IdEmployee')
    id = models.OneToOneField(User,on_delete=models.CASCADE,db_column='id')
    islogin = models.BooleanField(db_column='IsLogin', default=False,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'LaborPayments'

    def __str__(self) -> str:
        return 'login {}'.format(self.islogin)

class DocumentEmployee(models.Model):
    iddocument_employee = models.AutoField(db_column='IdDocumentEmployee', primary_key=True)
    iddocument_type = models.ForeignKey(DocumentType,on_delete=models.CASCADE,db_column='IdDocumentType')
    issue_date = models.DateField(db_column='Issue_Date',null=False,blank=False)
    expiration_date = models.DateField(db_column='Expiration_Date',null=False,blank=False)
    attachment = models.FileField(db_column='Attachment',upload_to='document/employee/', max_length=255,null=True,blank=True)
    procedure_cost = models.DecimalField(db_column='ProcedureCosto', max_digits=10, decimal_places=2,null=False,blank=False)
    observations = models.CharField(db_column='Observations', max_length=255,null=False,blank=False)
    idemployee = models.ForeignKey(Employee,on_delete=models.CASCADE,db_column='IdEmployee')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Target:
        managed = False
        db_table = 'DocumentEmployee'

    def __str__(self) -> str:
        return 'documeto {}'.format(self.iddocument_employee)