from rest_framework import serializers

from .models import Police, Doc, Client, UkrainePassport, IDCard, ForeignPassport


class PolicesListSerializer(serializers.ModelSerializer):
    """List of polices"""

    class Meta:
        model = Police
        fields = ("term", "cadastralNumber", "startDate")


class DocListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = "__all__"


class DocCreateSerializer(serializers.ModelSerializer):
    """Creating docs"""

    class Meta:
        model = Doc
        fields = "__all__"


class UkrainePassportCreateSerializer(serializers.ModelSerializer):
    """Create Ukraine passport"""

    class Meta:
        model = UkrainePassport
        fields = "__all__"


class IdPassportCreateSerializer(serializers.ModelSerializer):
    """Create idCard passport"""

    class Meta:
        model = IDCard
        fields = "__all__"


class ForeignPassportCreateSerializer(serializers.ModelSerializer):
    """Create foreign passport"""

    class Meta:
        model = ForeignPassport
        fields = "__all__"


class ClientCreateSerializer(serializers.ModelSerializer):
    """Create user"""

    class Meta:
        model = Client
        fields = "__all__"
