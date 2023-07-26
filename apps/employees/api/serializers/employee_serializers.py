from apps.employees.models import Employee, DocumentEmployee, IsLogin
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class ss(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idemployee': 1,
            'identificationcard': instance.identificationcard,
            'entry_date': instance.entry_date,
            'names': instance.names + ' ' + instance.lastnames,
            'address': instance.address,
            'location': instance.idlocation.location +' (' + instance.idlocation.idprovince.name + ' - ' + instance.idlocation.idprovince.idcountry.name +')',
            'position': instance.idposition.job_name,
            'period_payment': instance.idperiod_payment.period
        }

class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idemployee': instance.idemployee,
            'identificationcard': instance.identificationcard,
            'entry_date': instance.entry_date,
            'names': instance.names + ' ' + instance.lastnames,
            'photo': instance.photo.url if instance.photo != '' else '',
            'email': instance.email,
            'phone': instance.phone,
            'cell': instance.cell,
            'observations': instance.observations,
            'salary': instance.salary,
            'birth_date':  instance.birth_date,
            'address': instance.address,
            'location': instance.idlocation.location +' (' + instance.idlocation.idprovince.name + ' - ' + instance.idlocation.idprovince.idcountry.name +')',
            'position': instance.idposition.job_name,
            'period_payment': instance.idperiod_payment.period
        }

class DocumentEmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = DocumentEmployee
        fields = '__all__'

class DocumentEmployeeListSerializer (serializers.ModelSerializer):
    class Meta:
        model = DocumentEmployee
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'iddocument_employee': instance.iddocument_employee,
            'issue_date': instance.issue_date,
            'expiration_date': instance.expiration_date,
            'attachment': instance.attachment.url if instance.attachment != '' else '',
            'procedure_cost': instance.procedure_cost,
            'observations': instance.observations,
            'document_type': instance.iddocument_type.name,
            'idemployee': instance.idemployee.idemployee
        }


class IsLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = IsLogin
        fields = '__all__'

class IsLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = IsLogin
        fields = '__all__'