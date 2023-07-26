import re
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from apps.company.utils import validate_files
from apps.employees.api.serializers.employee_serializers import (
    EmployeeListSerializer, EmployeeSerializer, DocumentEmployeeSerializer, DocumentEmployeeListSerializer, IsLoginSerializer )
from apps.employees.models import Employee, DocumentEmployee, IsLogin


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    List_serializer_class = EmployeeListSerializer

    def get_queryset(self):
        return Employee.objects.all()

    def list(self, request):
        employee_serialize =  self.List_serializer_class(self.get_queryset(), many = True)
        return Response(employee_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = validate_files(request.data,'photo')
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empleado Correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        employee =  Employee.objects.filter(idemployee = pk).first()
        if employee:
            employee_serializer = self.serializer_class(employee)
            return Response(employee_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        data = validate_files(request.data,'photo', True)
        employee =  Employee.objects.filter(idemployee = pk).first()
        if employee:
            if employee:
                employee_serializer = self.serializer_class(employee,data = data)
                if employee_serializer.is_valid():
                    employee_serializer.save()
                    return Response({'message':'Empleado Correctamente'}, status=status.HTTP_200_OK)
            return Response({'erros': employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        employee = Employee.objects.filter(idemployee = pk).first()
        if employee:
            self.perform_destroy(self.get_object())
            return Response({'message':'Empleado Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class DocumentEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentEmployeeSerializer
    List_serializer_class = DocumentEmployeeListSerializer

    def get_queryset(self):
        return DocumentEmployee.objects.all()

    def list(self, request):
        documentemployee_serialize =  self.List_serializer_class(self.get_queryset(), many = True)
        return Response(documentemployee_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Creado Correctamente'},status= status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        documentemployee =  DocumentEmployee.objects.filter(iddocument_employee = pk).first()
        if documentemployee:
            documentemployee_serializer = self.serializer_class(documentemployee)
            return Response(documentemployee_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe este Documento'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        documentemployee =  DocumentEmployee.objects.filter(iddocument_employee = pk).first()
        if documentemployee:
            if documentemployee:
                documentemployee_serializer = self.serializer_class(documentemployee,data = request.data)
                if documentemployee_serializer.is_valid():
                    documentemployee_serializer.save()
                    return Response({'message':'Actualizado Correctamente'}, status=status.HTTP_200_OK)
            return Response(documentemployee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No hay el registro'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        documentemployee = DocumentEmployee.objects.filter(iddocument_employee = pk).first()
        if documentemployee:
            self.perform_destroy(self.get_object())
            return Response({'message':'Documento Eliminado Correctamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'Error de Eliminación'}, status=status.HTTP_400_BAD_REQUEST)

class IsLoginViewSet(viewsets.ModelViewSet):
    serializer_class = IsLoginSerializer

    def get_queryset(self):
        return IsLogin.objects.all()

class DocumentsEmployee(generics.ListAPIView):
    serializer_class = DocumentEmployeeListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return DocumentEmployee.objects.filter(idemployee= pk)

    def list(self, reques,pk=None):
        documentemployee_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(documentemployee_serializer.data, status=status.HTTP_200_OK)

class IsloginEmployee(generics.ListAPIView):
    serializer_class = IsLoginSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return IsLogin.objects.filter(id = pk)

    def list(self, request, pk=None):
        islogin_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(islogin_serializer.data, status=status.HTTP_200_OK)

class EmployeePosition(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Employee.objects.filter(idcompany = pk, idposition = 1)

    def list(self, request, pk=None):
        employee_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(employee_serializer.data, status=status.HTTP_200_OK)
