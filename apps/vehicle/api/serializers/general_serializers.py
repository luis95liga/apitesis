from apps.vehicle.models import Owner, VehicleUse, Axes, Manufacturer, VehicleType, Fuel, GeneralData,MaintenamceCosts, DocumentType

from rest_framework import serializers

class VehicleDocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'

class OwnerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        #fields = '__all__'

    def to_representation(self, instance):
      return{
         'idowner': instance.idowner,
         'name': instance.name,
         'company': instance.idcompany.name
      }

class VehicleUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleUse
        fields = '__all__'

class AxesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Axes
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleType
        fields = '__all__'

class FuelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fuel
        fields = '__all__'

class GeneralDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralData
        fields = '__all__'

class MaintenamceCostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenamceCosts
        fields = '__all__'

