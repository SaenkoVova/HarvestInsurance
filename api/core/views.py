from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, UkrainePassport, ForeignPassport, IDCard
from .serializers import RegistrationSerializer, LoginSerializer, ClientSerializer, UkrainePassportCreateSerializer, \
    ForeignPassportCreateSerializer, IDCardCreateSerializer, UkrainePassportListSerializer, \
    ForeignPassportListSerializer, IDCardListSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer

    def retrieve(self, request, *args, **kwargs):
        client = Client.objects.get(id=request.user)
        serializer = self.serializer_class(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        client = Client.objects.get(id=request.user)
        if client.check_password(serializer_data['password']):
            if serializer_data['new_password'] != '':
                serializer_data['password'] = serializer_data['new_password']
            serializer = self.serializer_class(
                client, data=serializer_data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(data="Wrong password", status=status.HTTP_400_BAD_REQUEST)


class DocumentCreateView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        tab = request.data.get('tab')
        doc = request.data.get('doc', {})
        doc['client'] = request.user
        if tab == 0:
            ukrainePassport = UkrainePassportCreateSerializer(data=doc)
            if ukrainePassport.is_valid(raise_exception=True):
                ukrainePassport.save()
                return Response(ukrainePassport.data, status=status.HTTP_200_OK)

        if tab == 2:
            foreignPassport = ForeignPassportCreateSerializer(data=doc)
            if foreignPassport.is_valid(raise_exception=True):
                foreignPassport.save()
                return Response(foreignPassport.data, status=status.HTTP_200_OK)
        if tab == 1:
            idCard = IDCardCreateSerializer(data=doc)
            if idCard.is_valid(raise_exception=True):
                idCard.save()
                return Response(idCard.data, status=status.HTTP_200_OK)


class DocumentsLoadView(APIView):

    def get(self, request):
        docs = []
        ukraine_passport = UkrainePassport.objects.filter(client_id=request.user)
        serializer = UkrainePassportListSerializer(ukraine_passport, many=True)
        if len(serializer.data):
            serializer.data[0]['type'] = 'ukraine_passport'
            docs.append(serializer.data[0])

        foreign_passport = ForeignPassport.objects.filter(client_id=request.user)
        serializer = ForeignPassportListSerializer(foreign_passport, many=True)
        if len(serializer.data):
            serializer.data[0]['type'] = 'foreign_passport'
            docs.append(serializer.data[0])

        id_card = IDCard.objects.filter(client_id=request.user)
        serializer = IDCardListSerializer(id_card, many=True)
        if len(serializer.data):
            serializer.data[0]['type'] = 'id_card'
            docs.append(serializer.data[0])

        return Response(docs, status=status.HTTP_200_OK)


class DocumentDestroyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        doc = request.GET['document']
        if doc == 'ukraine_passport':
            print(request.user)
            UkrainePassport.objects.filter(client_id=request.user).delete()
        if doc == 'foreign_passport':
            ForeignPassport.objects.filter(client_id=request.user).delete()
        if doc == 'id_card':
            IDCard.objects.filter(client_id=request.user).delete()

        return Response(status=status.HTTP_200_OK)
