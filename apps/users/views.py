from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializer import CustomTokenObtainPairSerializer, CustomUserSerializer, EmailSerializer, ResetPasswordSerializer
from apps.users.models import User
from apps.employees.models import IsLogin, Employee
from apps.employees.api.serializers.employee_serializers import EmployeeSerializer, IsLoginSerializer
from apps.users.utils import Util
from rest_framework.decorators import authentication_classes, permission_classes
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    serializer_class_login = IsLoginSerializer
    serializer_class_employee = EmployeeSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username=username,
            password=password) # User is authenticated

        if user:
            login_serializer = self.serializer_class(data=request.data)

            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                dd = user_serializer.data['id']
                islogin =  IsLogin.objects.filter(id = dd).first()
                if islogin:
                    islogin_serializer = self.serializer_class_login(islogin)
                    employee =  Employee.objects.filter(idemployee = islogin_serializer.data['idemployee']).first()
                    employee_serializer = self.serializer_class_employee(employee)
                    if islogin_serializer.data['islogin']:
                        return Response({
                            'token': login_serializer.validated_data.get('access'), # type: ignore
                            'refresh': login_serializer.validated_data.get('refresh'), # type: ignore
                            'idcompany': employee_serializer.data['idcompany'],
                            'idemployee': employee_serializer.data['idemployee'],
                            'user': user_serializer.data,
                            'message':'Inicio de sesion exitoso'
                        },status=status.HTTP_200_OK)
                    return Response ({'error': 'El Usuario no puede iniciar Sesion'}, status= status.HTTP_401_UNAUTHORIZED)
                return Response ({'error': 'El Usuario no puede iniciar Sesion'}, status= status.HTTP_401_UNAUTHORIZED)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'},status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Contraseña o nombre de usurio incorrectos'},status=status.HTTP_401_UNAUTHORIZED)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([])
@permission_classes([])
class PasswordResetView(GenericAPIView):

    serializer_class =  EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url_args = {'encoded_pk': encoded_pk, 'token': token}
            reset_url = reverse('reset-password', kwargs=reset_url_args)
            base_url = request.META['HTTP_ORIGIN']
            reset_url = f'{base_url}{reset_url}'
            email_body = 'Hola '+user.username + '\n \n Utilice el siguiente enlace para Restrablecer Su contraseña \n \n' + reset_url + '\n \n Gracias Por Utilizar nuestro Sito \n \n \n el equipo de trasporRouter'
            data = {'email_body': email_body, 'to_email': user.email,'email_subject': 'Restablecimieto de Contraseña'}
            Util.send_email(data)
            return Response({'message': 'Correo Enviado Correctamente'}, status= status.HTTP_200_OK)
        return Response({'message': "Usuario no existe con ese Correo Electronico"},status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([])
@permission_classes([])
class ResetPasswordAPIView(GenericAPIView):

    serializer_class = ResetPasswordSerializer

    @authentication_classes([])
    @permission_classes([])
    def post(self, request, **kwargs):

        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )