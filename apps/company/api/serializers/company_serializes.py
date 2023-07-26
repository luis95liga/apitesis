from apps.company.models import Company, TypeCompany, BankAccounts

from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idcompany':instance.idcompany,
            'name':instance.name,
            'logo': instance.logo.url if instance.logo != '' else '',
            'type_company':instance.idtype_company.name,
            'ruc':instance.ruc,
            'location':instance.idlocation.location,
            'address':instance.address,
            'email':instance.email,
            'phone':instance.phone,
            'tel_atcn_client':instance.tel_atcn_client,
            'cell':instance.cell,
            'default_load_type':instance.default_load_type
        }

class TypeCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeCompany
        fields = '__all__'

class BankAccountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccounts
        fields = '__all__'

class BankAccountsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccounts
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idbank_account':instance.idbank_account,
            'bank_name' :instance.bank_name,
            'account_number':instance.account_number,
            'default':instance.default,
            'company':instance.idcompany.name
        }

class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
      model = Company
      fields = '__all__'

    def to_representation(self, instance):
        return {
            'idcompany':instance.idcompany,
            'name':instance.name,
            'logo': instance.logo.url if instance.logo != '' else '',
            'type_company':instance.idtype_company.name,
            'ruc':instance.ruc,
            'location':instance.idlocation.location,
            'province':instance.idlocation.idprovince.name,
            'country':instance.idlocation.idprovince.idcountry.name,
            'address':instance.address,
            'email':instance.email,
            'phone':instance.phone,
            'tel_atcn_client':instance.tel_atcn_client,
            'cell':instance.cell,
            'default_load_type':instance.default_load_type
        }