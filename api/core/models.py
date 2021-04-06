# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Doc(models.Model):
    passportIssue = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Doc'


class Client(models.Model):
    secondName = models.CharField(max_length=20, blank=False, null=False)
    firstName = models.CharField(max_length=20, blank=False, null=False)
    thirdName = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=20, blank=False, null=False)
    birthDate = models.DateField(blank=False, null=False)
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Client'


class ForeignPassport(models.Model):
    seriesAndNumber = models.CharField(max_length=20, blank=True, null=True)
    doc = models.OneToOneField(Doc, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'ForeignPassport'


class IDCard(models.Model):
    issuedBy = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    notation = models.CharField(max_length=20, blank=True, null=True)
    doc = models.OneToOneField(Doc, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'IDCard'


class InsuredEvent(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    hint = models.CharField(max_length=100, blank=False, null=False)
    impactPrice = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'InsuredEvent'


class Police(models.Model):
    geoJson = models.TextField(blank=False, null=False)
    cadastralNumber = models.CharField(max_length=20, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    term = models.IntegerField(blank=False, null=False)
    coating = models.FloatField(blank=False, null=False)
    startDate = models.DateField(blank=False, null=False)
    ensuredEvents = models.ManyToManyField(InsuredEvent)

    class Meta:
        db_table = 'Police'


class UkrainePassport(models.Model):
    seriesAndNumber = models.CharField(max_length=20, blank=False, null=False)
    issuedBy = models.CharField(blank=False, null=False, max_length=20)
    doc = models.OneToOneField(Doc, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'UkrainePassport'
