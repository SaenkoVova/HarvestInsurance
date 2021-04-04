# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    clientid = models.IntegerField(primary_key=True)
    secondname = models.CharField(max_length=20, blank=True, null=True)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    thirdname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    docid = models.ForeignKey('Doc', models.DO_NOTHING, db_column='docid')

    class Meta:
        db_table = 'client'
        unique_together = (('clientid', 'docid'),)


class Doc(models.Model):
    docid = models.CharField(primary_key=True, max_length=18)
    passportissue = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'doc'


class Foreignpassport(models.Model):
    seriesandnumber = models.CharField(max_length=20, blank=True, null=True)
    docid = models.OneToOneField(Doc, models.DO_NOTHING, db_column='docid', primary_key=True)

    class Meta:
        db_table = 'foreignpassport'


class Idcard(models.Model):
    issuedby = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    notation = models.CharField(max_length=20, blank=True, null=True)
    docid = models.OneToOneField(Doc, models.DO_NOTHING, db_column='docid', primary_key=True)

    class Meta:
        db_table = 'idcard'


class Insuredevent(models.Model):
    description = models.CharField(max_length=20, blank=True, null=True)
    hint = models.CharField(max_length=20, blank=True, null=True)
    eventid = models.IntegerField(primary_key=True)
    impactprice = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'insuredevent'


class Police(models.Model):
    policeid = models.IntegerField(primary_key=True)
    geojson = models.CharField(max_length=20, blank=True, null=True)
    cadastralnumber = models.CharField(max_length=20, blank=True, null=True)
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='clientid', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    coating = models.IntegerField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    docid = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        db_table = 'police'


class Ukrainepassport(models.Model):
    seriesandnumber = models.CharField(max_length=20, blank=True, null=True)
    issuedby = models.DateField(blank=True, null=True)
    docid = models.OneToOneField(Doc, models.DO_NOTHING, db_column='docid', primary_key=True)

    class Meta:
        db_table = 'ukrainepassport'
