from base64 import urlsafe_b64decode
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
   pass

class CustomUserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ('id','username','email','name','last_name','is_superuser', 'is_active')

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = '__all__'

   def create(self, validated_data):
      user = User(**validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user

   def update(self, instance, validated_data):
      updated_user = super().update(instance,validated_data)
      updated_user.set_password(validated_data['password'])
      updated_user.save()
      return updated_user

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class UserListSerializer(serializers.ModelSerializer):
   class Meta:
      model = User

   def to_representation(self, instance):
      return{
         'id': instance['id'],
         'username': instance['username'],
         'email': instance['email'],
         'name': instance['name'],
         'password': instance['password']
      }


class EmailSerializer(serializers.Serializer):

   email = serializers.EmailField()

   class Meta:
      fields = ('email')


class ResetPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        field = ("password","password2")

    def validate(self, data):
      password = data.get("password")
      password = data.get("password2")
      token = self.context.get("kwargs").get("token") # type: ignore
      encoded_pk = self.context.get("kwargs").get("encoded_pk") # type: ignore

      if token is None or encoded_pk is None:
         raise serializers.ValidationError("Error de Url")

      pk = urlsafe_base64_decode(encoded_pk).decode()
      user = User.objects.get(pk=pk)
      if not PasswordResetTokenGenerator().check_token(user, token):
         raise serializers.ValidationError("Esta Url es Invalida")
      if data['password'] != data['password2']:
            raise serializers.ValidationError(
               {'password':'Debe ingresar ambas contraseñas iguales'}
            )
      user.set_password(password)
      user.save()
      return data