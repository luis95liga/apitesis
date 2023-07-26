from apps.employees.models import DocumentType, PeriodPayment, PositionType, Position, LaborPayments
from rest_framework import serializers

class EmployeesDocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        fields = '__all__'

class PeriodPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodPayment
        fields = '__all__'

class PositionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionType
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'

class PositionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'

    def to_representation(self, instance):
        return{
        'idposition': instance.idposition,
        'job_name': instance.job_name,
        'position_type': instance.idposition_type.job_type_name
        }

class LaborPaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LaborPayments
        fields = '__all__'
