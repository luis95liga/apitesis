from rest_framework import serializers
from apps.routes.models import Cellars, Destinations, Tabulation, Bill, Concepts


class CellarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cellars
        fields = '__all__'


class CellarsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cellars
        fields = '__all__'
    def to_representation(self, instance):
        return {
            'idcellars':instance.idcellars,
            'cellar':instance.cellar,
            'state':instance.state,
            'province':instance.idprovince.name
        }

class DestinationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destinations
        fields = '__all__'


class DestinationsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destinations
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'iddestinations':instance.iddestinations,
            'destinations':instance.destinations,
            'state':instance.state,
            'province':instance.idprovince.name
        }

class TabulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tabulation
        fields = '__all__'

class TabulationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tabulation
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idtabulation': instance.idtabulation,
            'location':instance.idlocation.location,
            'destinations':instance.iddestinations.destinations,
            'km':instance.km,
            'hours':instance.hours,
            'idcompany': instance.idcompany.idcompany
        }

class ConceptsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concepts
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'

class BillListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idbill': instance.idbill,
            'concepts':instance.idconcepts.concepts,
            'amount':instance.amount,
            'idcompany': instance.idcompany.idcompany,
            'idtabulation': instance.idtabulation.idtabulation
        }
