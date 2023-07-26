from apps.company.models import Country, Locality, Province, DocumentType, Documents

from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'


class LocalitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Locality
        fields = '__all__'
        
class LocalityListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Locality
        fields = '__all__'
    def to_representation(self, instance):
        return {
            'idlocation':instance.idlocation,
            'location':instance.location,
            'state':instance.state,
            'province':instance.idprovince.name
        }
        
class ProvinceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Province
        fields = '__all__'
        
class ProvinceListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Province
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'idprovince': instance.idprovince,
            'country': instance.idcountry.name,
            'name': instance.name,
        }
        
class DocumentTypeSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = DocumentType
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'


class DocumentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'iddocument': instance.iddocument,
            'type_document': instance.idtype_document.name,
            'issue_date': instance.issue_date,
            'expiration_date': instance.expiration_date,
            'attachment': instance.attachment.url if instance.attachment != '' else '',
            'cost_procedure': instance.cost_procedure,
            'observations': instance.observations,
            'idcompany': instance.idcompany.idcompany
        }
