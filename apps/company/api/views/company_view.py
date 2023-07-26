from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from apps.company.utils import validate_files
from apps.company.models import (
    Company,
    BankAccounts,
    TypeCompany
)
from apps.company.api.serializers.company_serializes import (
    BankAccountsListSerializer,
    BankAccountsSerializer,
    CompanyListSerializer,
    CompanySerializer,
    TypeCompanySerializer,
    CompanyNameSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    list_serializer_class = CompanyListSerializer

    def get_queryset(self):
        return Company.objects.all()

    def list(self, request):
        company_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(company_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = validate_files(request.data,'logo')
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Compania creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        company =  Company.objects.filter(idcompany = pk).first()
        if company:
            company_serializer = self.serializer_class(company)
            return Response(company_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        data = validate_files(request.data,'logo', True)
        company =  Company.objects.filter(idcompany = pk).first()
        if company:
            if company:
                company_serializer = self.serializer_class(company,data = data)
                if company_serializer.is_valid():
                    company_serializer.save()
                    return Response({'message':'Compañia Actualizada Correctamente'}, status=status.HTTP_200_OK)
                return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        company =  Company.objects.filter(idcompany = pk).first()
        if company:
            self.perform_destroy(self.get_object())
            return Response({'message':'Compañia Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class BankAccountsViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountsSerializer
    list_serializer_class = BankAccountsListSerializer

    def get_queryset(self):
        return BankAccounts.objects.all()

    def list(self, request):
        bankaccounts_serialize =  self.list_serializer_class(self.get_queryset(), many = True)
        return Response(bankaccounts_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'cuenta creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        bankaccounts =  BankAccounts.objects.filter(idbank_account = pk).first()
        if bankaccounts:
            bankaccounts_serializer = self.serializer_class(bankaccounts)
            return Response(bankaccounts_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        bankaccounts =  BankAccounts.objects.filter(idbank_account = pk).first()
        if bankaccounts:
            if bankaccounts:
                print(request.data)
                bankaccounts_serializer = self.serializer_class(bankaccounts,data = request.data)
                if bankaccounts_serializer.is_valid():
                    bankaccounts_serializer.save()
                    return Response({'message':'Cuenta Bancaria Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(bankaccounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        bankaccounts =  BankAccounts.objects.filter(idbank_account = pk).first()
        if bankaccounts:
            self.perform_destroy(self.get_object())
            return Response({'message':'Cuenta Bancaria Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class TypeCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = TypeCompanySerializer

    def get_queryset(self):
        return TypeCompany.objects.all()

    def list(self, request):
        typecompany_serialize =  self.serializer_class(self.get_queryset(), many = True)
        return Response(typecompany_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de Comapañia creada correctmente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        typecompany =  TypeCompany.objects.filter(idtype_company = pk).first()
        if typecompany:
            typecompany_serializer = self.serializer_class(typecompany)
            return Response(typecompany_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        typecompany =  TypeCompany.objects.filter(idtype_company = pk).first()
        if typecompany:
            if typecompany:
                typecompany_serializer = self.serializer_class(typecompany,data = request.data)
                if typecompany_serializer.is_valid():
                    typecompany_serializer.save()
                    return Response({'message':'Tipo de Comapañia Actualizada Correctamente'}, status=status.HTTP_200_OK)
            return Response(typecompany_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        typecompany =  TypeCompany.objects.filter(idtype_company = pk).first()
        if typecompany:
            self.perform_destroy(self.get_object())
            return Response({'message':'Tipo de Comapañia Eliminada Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class BankAccountCompany(generics.ListAPIView):
    serializer_class = BankAccountsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return BankAccounts.objects.filter(idcompany = pk)

    def list(self, request, pk=None):
        bankaccounts = BankAccounts.objects.filter(idcompany = pk)
        if bankaccounts:
            bankaccounts_serializer = self.serializer_class(bankaccounts, many = True)
            return Response(bankaccounts_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay Datos'},status= status.HTTP_400_BAD_REQUEST);

class CompanyName(generics.ListAPIView):
    serializer_class = CompanyNameSerializer

    def get_queryset(self):
        return Company.objects.all()

    def list(self, request, pk=None):
        company = Company.objects.filter(idcompany = pk).first()
        if company:
            company_serializer = self.serializer_class(company)
            return Response(company_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No hay Datos'},status= status.HTTP_400_BAD_REQUEST);