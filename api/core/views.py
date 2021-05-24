import io
import json
import os
from django.http import FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import numpy
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from zipfile import ZipFile
from osgeo import gdal
import rasterio
import rasterio.mask
from dateutil import parser
import fiona

from .models import Client, UkrainePassport, ForeignPassport, IDCard, Police, Notification
from .serializers import RegistrationSerializer, LoginSerializer, ClientSerializer, UkrainePassportCreateSerializer, \
    ForeignPassportCreateSerializer, IDCardCreateSerializer, UkrainePassportListSerializer, \
    ForeignPassportListSerializer, IDCardListSerializer, NotificationsRetrieveSerializer, \
    OrderDetailsRetrieveSerializer, \
    OrdersRetrieveSerializer
from django.conf import settings


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        print(user)

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


class NotificationsLoadView(APIView):

    def get(self, request):
        client = Client.objects.get(id=request.user)
        notifications = client.notifications.all()
        serializer = NotificationsRetrieveSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationsReadView(APIView):

    def get(self, request):
        client = Client.objects.get(id=request.user)
        notifications = client.notifications.filter(state='unread')
        for note in notifications:
            note.state = 'read'
            note.save()
        return Response(status=status.HTTP_200_OK)


class NotificationsDeleteView(APIView):

    def get(self, request):
        notification_id = request.GET['notificationId']
        Notification.objects.filter(id=notification_id).delete()
        return Response(status=status.HTTP_200_OK)


class DocumentDestroyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        doc = request.GET['document']
        if doc == 'ukraine_passport':
            UkrainePassport.objects.filter(client_id=request.user).delete()
        if doc == 'foreign_passport':
            ForeignPassport.objects.filter(client_id=request.user).delete()
        if doc == 'id_card':
            IDCard.objects.filter(client_id=request.user).delete()

        return Response(status=status.HTTP_200_OK)


class CalculatePriceView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        checkout = request.data.get('checkout')
        print(checkout)
        return Response(100, status=status.HTTP_200_OK)


class OrdersLoadView(APIView):

    def get(self, request):
        client = Client.objects.get(id=request.user)
        polices = client.polices.all()
        serializer = OrdersRetrieveSerializer(polices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailsLoadView(APIView):

    def get(self, request):
        police_id = request.GET['police_id']
        print(police_id)
        police = Police.objects.get(id=police_id)
        serializer = OrderDetailsRetrieveSerializer(police, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


def read_lut(lut_fn):  # this function reads the color-table from LUT file
    lut_entries = 256
    lut = numpy.loadtxt(lut_fn)
    assert len(lut) >= lut_entries
    assert lut.shape[1] >= 4
    return lut


def add_lut(lut_fn, data_fn):  # add color-table to the GeoTIFF file
    lut_entries = 256
    lut = read_lut(lut_fn)
    in_dataset = gdal.Open(data_fn, gdal.GF_Write)
    band = in_dataset.GetRasterBand(1)
    color_table = gdal.ColorTable()

    for i, entry in enumerate(lut[:lut_entries]):
        entry = tuple(int(max(0, min(255, 255 * u))) for u in entry)
        color_table.SetColorEntry(i, entry)
    band.SetColorTable(color_table)
    in_dataset.FlushCache()
    del in_dataset


def make_ndvi(path, bands, band_list, color_mode, user_id):
    required_bands = {'b08', 'b04'}
    red_name = [item for item in band_list if item[-7:-4].lower() == 'b04']
    nir_name = [item for item in band_list if item[-7:-4].lower() == 'b08']
    if required_bands.intersection(bands) == required_bands:
        with rasterio.open(path + red_name[0]) as red:
            with rasterio.open(path + nir_name[0]) as nir:
                b4 = red.read(1)  # reading red band
                b8 = nir.read(1)  # reading NIR band
                numpy.seterr(divide='ignore', invalid='ignore')
                ndvi = (((b8 - b4) / (b8 + b4)) * 255).astype(numpy.uint8)  # making NDVI [Vegetation Index FORMULA]

                ndvi[ndvi > 253] = 253  # filtering service values

                kwargs = red.meta
                kwargs.update(dtype=rasterio.uint8, driver='GTiff')

                raster_file = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}', 'rasters',
                                           red_name[0][:-7] + "NDVI.TIF")

                with rasterio.open(raster_file, 'w', **kwargs) as dst:
                    dst.write(ndvi, indexes=1)

                if color_mode:
                    add_lut('d:\\Education\\graduateWork\\task2\\ndvi_palette.lut',
                            raster_file)
                return True
    else:
        print("not all band required for NDVI found")
        return False


def parse_date(file_name):
    for el in file_name.split('_'):
        if len(el) == 15:
            return parser.parse(el.split('T')[0]).date()


def get_weighted_average(arr):
    (unique, counts) = numpy.unique(arr, return_counts=True)
    for g in range(len(unique)):
        unique[g] = unique[g] * counts[g] / sum(counts)
    return round(sum(unique), 3)


class CreatePoliceView(APIView):

    def post(self, request):
        order = request.data.get('order')
        print(order)
        user_id = request.user
        user_folder = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}')
        orders_folders = os.path.join(settings.STATIC_DIR, 'orders')
        zipes_directory = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}', 'zipes')
        reprojected_directory = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}', 'reprojected')
        extract_directory = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}', 'extract')
        rasters_directory = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}', 'rasters')
        field_directory = os.path.join(settings.STATIC_DIR, 'sentinels', f'user_{user_id}', 'field')
        for file in os.listdir(zipes_directory):
            with ZipFile(os.path.join(zipes_directory, file), 'r') as zip:
                zip.extractall(path=extract_directory)

        for folder in os.listdir(extract_directory):
            path_to_granule = os.path.join(extract_directory, folder, 'GRANULE')
            for granule_folder in os.listdir(path_to_granule):
                path = os.path.join(path_to_granule, granule_folder, 'IMG_DATA') + '\\'
                bands_list = os.listdir(path)
                bands = {item[-7:-4].lower() for item in bands_list}
                if make_ndvi(path, bands, bands_list, True, user_id):
                    print(path, 'completed')

        schema = {'geometry': 'Polygon', 'properties': {'fld_a': 'str:50'}}
        with fiona.open(os.path.join(user_folder, 'polygon.shp'), 'w', 'ESRI Shapefile', schema, crs='EPSG:4326') as layer:
            layer.write({'geometry': json.loads(order['geoJson']), 'properties': {'fld_a': 'test'}})

        for raster in os.listdir(rasters_directory):
            ds = gdal.Open(os.path.join(rasters_directory, raster))
            gdal.Warp(os.path.join(reprojected_directory, raster), ds, dstSRS='EPSG:4326')

        with fiona.open(os.path.join(user_folder, 'polygon.shp'), "r") as shapefile:
            shapes = [feature["geometry"] for feature in shapefile]
            for raster in os.listdir(reprojected_directory):
                with rasterio.open(os.path.join(reprojected_directory, raster)) as src:
                    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
                    out_meta = src.meta

                out_meta.update({"driver": "GTiff",
                                 "height": out_image.shape[1],
                                 "width": out_image.shape[2],
                                 "transform": out_transform})

                with rasterio.open(os.path.join(field_directory, raster), "w", **out_meta) as dest:
                    dest.write(out_image)

                add_lut('d:\\Education\\graduateWork\\task2\\ndvi_palette.lut', os.path.join(field_directory, raster))
        values = []
        dates = []
        for field in os.listdir(field_directory):
            with rasterio.open(os.path.join(field_directory, field)) as ds:
                arr = ds.read()
                weighted_avg = get_weighted_average(arr)
                parsed_date = parse_date(field)
                if weighted_avg > 0 and 3 < parsed_date.month < 10:
                    values.append(weighted_avg)
                    dates.append(parsed_date)

        client = Client.objects.get(id=request.user)

        police = Police(geoJson=order['geoJson'], cadastralNumber=order['cadastralNumber'],
                        price=order['price'], term=order['term'], coating=order['coating'], startDate=order['startDate'],
                        docType=order['docType'], docId=order['docId'], status=order['status'], ndvi=values, dates=dates)
        police.save()
        client.polices.add(police)
        notification = Notification(notes='police_created')
        notification.save()
        client.notifications.add(notification)
        client = Client.objects.get(id=request.user)
        c = canvas.Canvas(os.path.join(orders_folders, 'Police_' + police.id + '_user_' + str(request.user)))
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 14)
        c.drawString(50, 800, u'Страховий договір')
        c.drawString(50, 740, u'Дата народження: ' + str(client.birth_date))
        c.drawString(50, 710, u'Електронна пошта: ' + client.email)
        c.drawString(50, 680, u'Мобільний телефон: ' + client.email)
        c.drawString(50, 650, u'Місцезнаходження майна: ' + order['geoJson'])
        c.drawString(50, 620, u'Загальна страхова сума за договором: ' + order['coating'])
        c.showPage()
        c.save()

        return Response(status=status.HTTP_201_CREATED)
