from rest_framework import serializers

from .models import Client


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Client
        fields = ['token', 'email', 'username', 'first_name', 'second_name', 'third_name', 'docs', 'polices', 'phone',
                  'birth_date', 'password']

    def create(self, validated_data):
        return Client.objects.create_user(**validated_data)
