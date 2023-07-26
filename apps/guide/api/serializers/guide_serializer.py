from rest_framework import serializers
from apps.guide.models import *

class GuideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = '__all__'


class GuideListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idguide': instance.idguide,
            'km': instance.km,
            'hours': instance.hours,
            'status': instance.status,
            'client': instance.idclient.names + ' ' + instance.idclient.lastnames,
            'company': instance.idcompany.name,
            'idcompany': instance.idcompany.idcompany,
            'location': instance.idlocation.location,
            'destinations': instance.iddestinations.destinations,
            'idvehicle': instance.idvehicle.idvehicle,
            'iduser': instance.iduser
            }

class GuideListTravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idguide': instance.idguide,
            'km': instance.km,
            'hours': instance.hours,
            'status': instance.status,
            'idclient': instance.idclient,
            'client': instance.idclient.names + ' ' + instance.idclient.lastnames,
            'idcompany': instance.idcompany.idcompany,
            'company': instance.idcompany.name,
            'idlocation': instance.idlocation.idlocation,
            'location': instance.idlocation.location,
            'destinations': instance.iddestinations.destinations,
            'iddestinations': instance.iddestinations.destinations,
            'idvehicle': instance.idvehicle.idvehicle,
            'iduser': instance.iduser
            }

class TravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = '__all__'

class TravelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idtravel': instance.idtravel,
            'hours': instance.hours,
            'kms': int(instance.kms) + int(instance.kmsdes),
            'total': instance.total,
            'idtrailer': instance.idtrailer.idtrailer,
            'idvehicle': instance.idvehicle.idvehicle
        }

class GuideLocationLatitudeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idguide': instance.idguide,
            'km': instance.km,
            'hours': instance.hours,
            'rute': '{} -> {}'.format( instance.idlocation.location, instance.iddestinations.destinations ),
            'idlocation': instance.idlocation.idlocation,
            'Olatitude': instance.idlocation.latitude,
            'Olongitude': instance.idlocation.longitude,
            'iddestinations': instance.iddestinations.iddestinations,
            'Dlatitude': instance.iddestinations.latitude,
            'Dlongitude': instance.iddestinations.longitude,
            }

class InvoiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceType
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'

class GuideContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuideContent
        fields = '__all__'

class GuideContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuideContent
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'idguidecontent': instance.idguidecontent,
            'idguide': instance.idguide.idguide,
            'invoicetype': instance.idinvoicetype.invoicetype,
            'authorizacionno': instance.authorizacionno,
            'receiptno': instance.receiptno,
            'customsdeclarationnumber': instance.customsdeclarationnumber,
            'reasonfortransfer': instance.reasonfortransfer
        }

class GuideContentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuideContentDetail
        fields = '__all__'

class GuideContentDetailListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuideContentDetail
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idguidecontentdetail': instance.idguidecontentdetail,
            'idguidecontent': instance.idguidecontent.idguidecontent,
            'description': instance.description,
            'unit': instance.idunit.unit,
            'amount': instance.amount
        }

class GuideContentDetailTmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuideContentDetailTmp
        fields = '__all__'

class GuideContentDetailTmpListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuideContentDetailTmp
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idguidecontentdetailtmp': instance.idguidecontentdetailtmp,
            'idguide': instance.idguide.idguide,
            'idemployee': instance.idemployee.idemployee,
            'description': instance.description,
            'unit': instance.idunit.unit,
            'amount': instance.amount
        }


class GuideListViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idguide': instance.idguide,
            'km': instance.km,
            'hours': instance.hours,
            'status': instance.status,
            'client': instance.idclient.names + ' ' + instance.idclient.lastnames,
            'identificationcard': instance.idclient.identificationcard,
            'company': instance.idvehicle.idemployee.names + ' ' + instance.idvehicle.idemployee.lastnames,
            'ruc': instance.idvehicle.idemployee.identificationcard,
            'idcompany': instance.idvehicle.idemployee.idemployee,
            'location': instance.idlocation.location,
            'destinations': instance.iddestinations.destinations,
            'idvehicle': instance.idvehicle.idvehicle,
            'tuition': instance.idvehicle.tuition,
            }

