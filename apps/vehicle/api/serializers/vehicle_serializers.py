from apps.vehicle.models import FixedCosts, TechnicalData, Vehicle, VehicleModel, Trailer, TechnicalDataTrailer, DocumentType, DocumentVehicle, AssignTrailer
from rest_framework import serializers

class TechnicalDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicalData
        fields = '__all__'

class TechnicalDataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicalData
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idtechnical_data': instance.idtechnical_data,
            'load_capacity': instance.load_capacity,
            'color': instance.color,
            'mileage': instance.mileage,
            'fuel': instance.idfuel.type_fuel,
            'hours_use' : instance.hours_use,
            'tank_capacity' : instance.tank_capacity,
            'yield_gallon' : instance.yield_gallon,
            'observation' : instance.observation,
            'year': instance.year,
            'idgps': instance.idgps,
        }

class TechnicalDataTrailerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicalDataTrailer
        fields = '__all__'

class TechnicalDataTrailerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicalDataTrailer
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idtechnical_datatrailer': instance.idtechnical_datatrailer,
            'load_capacity': instance.load_capacity,
            'color': instance.color,
            'hours_use' : instance.hours_use,
            'observation' : instance.observation,
            'idadministrative_data': instance.idadministrative_data,
        }

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        exclude = ('create_date',)


class VehicleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        exclude = ('create_date',)
        #fields = '__all__'

    def to_representation(self, instance):
        return {
            'idvehicle': instance.idvehicle,
            'owner':instance.idowner.name,
            'vehicle_model':instance.idvehicle_model.model,
            'idemployee':instance.idemployee.idemployee,
            'employee':instance.idemployee.names + ' ' + instance.idemployee.lastnames,
            'vehicle_use':instance.idvehicle_use.vehicle_use,
            'agination_date':instance.agination_date,
            'tuition':instance.tuition,
            'engine_series':instance.engine_series,
            'state':instance.state,
            'idtechnical_data': instance.idtechnical_data.idtechnical_data,
        }

class TrailerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trailer
        exclude = ('create_date',)

class TrailerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trailer
        exclude = ('create_date',)
        #fields = '__all__'

    def to_representation(self, instance):
        return {
            'idtrailer': instance.idtrailer,
            'owner':instance.idowner.name,
            'vehicle_model':instance.idvehicle_model.model,
            'vehicle_use':instance.idvehicle_use.vehicle_use,
            'tuition':instance.tuition,
            'state':instance.state,
            'idtechnical_datatrailer': instance.idtechnical_datatrailer.idtechnical_datatrailer,
        }

class VehicleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleModel
        fields = '__all__'

class VehicleModelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleModel
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idvehicle_model': instance.idvehicle_model,
            'manufacturer':  instance.idmanufacturer.name,
            'model':instance.model,
            'year':instance.year,
            'vehicle_type':instance.idvehicle_type.name,
            'kind':instance.kind,
            'fuel':instance.idfuel.type_fuel,
            'axis':instance.idaxis.name,

        }


class VehicleViewSerializer(serializers.ModelSerializer):
    idtechnical_data = TechnicalDataSerializer()
    class Meta:
        model = Vehicle
        exclude = ('create_date',)

class TrailerViewSerializer(serializers.ModelSerializer):
    idtechnical_datatrailer = TechnicalDataTrailerSerializer()
    class Meta:
        model = Trailer
        exclude = ('create_date',)



class DocumentVehicleSerializer (serializers.ModelSerializer):
    class Meta:
        model = DocumentVehicle
        fields = '__all__'

class DocumentVehicleListSerializer (serializers.ModelSerializer):
    class Meta:
        model = DocumentVehicle
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'iddocument_vehicle': instance.iddocument_vehicle,
            'issue_date': instance.issue_date,
            'expiration_date': instance.expiration_date,
            'attachment': instance.attachment.url if instance.attachment != '' else '',
            'procedure_cost': instance.procedure_cost,
            'observations': instance.observations,
            'document_type': instance.iddocument_type.name,
            'idvehicle': instance.idvehicle.idvehicle
        }

class AssignTrailerSerializer (serializers.ModelSerializer):
     class Meta:
        model = AssignTrailer
        fields = '__all__'

class FixedCostsSerializer (serializers.ModelSerializer):
     class Meta:
        model = FixedCosts
        fields = '__all__'