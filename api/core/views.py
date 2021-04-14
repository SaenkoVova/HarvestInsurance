from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Police, Doc
from .serializers import PolicesListSerializer, DocCreateSerializer, DocListSerializer, ClientCreateSerializer, \
    UkrainePassportCreateSerializer, IdPassportCreateSerializer, ForeignPassportCreateSerializer


class PolicesListView(APIView):
    def get(self, request):
        polices = Police.objects
        serializer = PolicesListSerializer(polices, many=True)
        return Response(serializer.data)


class DocListView(APIView):
    def get(self, request):
        docs = Doc.objects
        serializer = DocListSerializer(docs, many=True)
        return Response(serializer.data)


class DocCreateView(APIView):
    """Add docs"""

    def post(self, request):
        doc = DocCreateSerializer(data=request.data)
        if doc.is_valid():
            doc.save()
        return Response(status=201)


class UkrainePassportCreateView(APIView):
    """Add ukraine passport"""

    def post(self, reuest):
        ukrainePassport = UkrainePassportCreateSerializer(data=reuest.data)
        if ukrainePassport.is_valid():
            ukrainePassport.save()
        return Response(status=201)


class ClientCreateView(APIView):
    """Add client"""

    def post(self, request):
        payload = request.data
        passport = None
        doc = DocCreateSerializer(data={'passportIssue': payload['doc']['passportIssue']})
        if doc.is_valid():
            doc = doc.save()
        if payload['currentTab'] == 0:

            passport = UkrainePassportCreateSerializer(data={
                'seriesAndNumber': payload['doc']['seriesAndNumber'],
                'issuedBy': payload['doc']['issuedBy'],
                'doc': doc.id
            })

        elif payload['currentTab'] == 1:
            passport = IdPassportCreateSerializer(data={
                'issuedBy': payload['doc']['issuedBy'],
                'number': payload['doc']['number'],
                'notation': payload['doc']['note'],
                'doc': doc.id
            })

        elif payload['currentTab'] == 2:
            passport = ForeignPassportCreateSerializer(data={
                'seriesAndNumber': payload['doc']['seriesAndNumber'],
                'doc': doc.id
            })
        if passport.is_valid():
            passport.save()
        payload['user']['doc'] = doc.id
        print(payload['user'])
        client = ClientCreateSerializer(data=payload['user'])
        if client.is_valid():
            client.save()
        return Response(status=201)
