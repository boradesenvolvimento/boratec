from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    admission = serializers.DateField()
    phone = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password", "admission", "phone", "first_name", "last_name"]

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email já cadastrado")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user
    
    def update(self, user, validated_data):
        user.password = validated_data.get('password', user.password)
        user.phone = validated_data.get('phone', user.phone)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)

        user.save()

        return user
    