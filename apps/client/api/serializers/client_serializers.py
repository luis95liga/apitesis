from apps.client.models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'
        
class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'idclient': instance.idclient,
            'identificationcard': instance.identificationcard,
            'entry_date': instance.entry_date,
            'names': instance.names + ' ' + instance.lastnames,
            'photo': instance.photo.url if instance.photo != '' else '',
            'email': instance.email,
            'phone': instance.phone,
            'cell': instance.cell,
            'observations': instance.observations,
            'birth_date':  instance.birth_date,
            'address': instance.address,
            'destinations': instance.iddestinations.destinations +' (' + instance.iddestinations.idprovince.name + ' - ' + instance.iddestinations.idprovince.idcountry.name +')',
        }