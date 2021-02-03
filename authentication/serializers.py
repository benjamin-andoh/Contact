from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=90, min_length=4, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=4)
    last_name = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        '''this gets is called before an instance is creaed
        we are using it to validate the fields'''
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'user with this email already exist'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=90, min_length=4, write_only=True)
    username = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model=User
        fields = ['username', 'password']
