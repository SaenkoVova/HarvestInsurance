from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Client, UkrainePassport, ForeignPassport, IDCard, Police, Notification


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Client
        fields = ['token', 'email']

    def create(self, validated_data):
        return Client.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('A password is required to log in')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'email', 'first_name', 'second_name', 'third_name', 'phone', 'token', 'birth_date', 'password')

        read_only_fields = ('token',)

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class UkrainePassportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UkrainePassport

        fields = '__all__'


class ForeignPassportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignPassport

        fields = '__all__'


class IDCardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDCard

        fields = '__all__'


class UkrainePassportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UkrainePassport
        fields = ['id', 'series_and_number', 'passport_issue', 'issued_by']


class ForeignPassportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignPassport
        fields = ['id', 'series_and_number', 'passport_issue']


class IDCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignPassport
        fields = ['id', 'issued_by', 'passport_issue', 'number', 'notation']


class OrdersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Police
        fields = ['id', 'cadastralNumber', 'status', 'startDate', 'term']


class OrderDetailsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Police
        fields = '__all__'


class NotificationsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
