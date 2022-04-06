# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flight(models.Model):
    id = models.TextField(primary_key=True)
    callsign = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    typecode = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    airline = models.TextField( blank=True, null=True)
    duration = models.BigIntegerField( blank=True, null=True)
    origin_city = models.TextField(blank=True, null=True)
    destination_city = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight'

class Flightplane(models.Model):
    id = models.TextField(primary_key=True)
    typecode = models.TextField(blank=True, null=True)
    date = models.DateField( blank=True, null=True)  # Field name made lowercase.
    month = models.BigIntegerField( blank=True, null=True)
    year = models.BigIntegerField( blank=True, null=True)
    airline = models.TextField( blank=True, null=True)
    count = models.BigIntegerField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flightplane'

class Flightlist(models.Model):
    id = models.TextField(primary_key=True)
    number = models.TextField(blank=True, null=True)
    date = models.DateField( blank=True, null=True)  # Field name made lowercase.
    month = models.BigIntegerField( blank=True, null=True)
    year = models.BigIntegerField( blank=True, null=True)
    airline = models.TextField( blank=True, null=True)
    count = models.BigIntegerField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flightlist'


class Flightroute(models.Model):
    id = models.TextField(primary_key=True)
    date = models.DateField( blank=True, null=True)  # Field name made lowercase.
    month = models.TextField(blank=True, null=True)
    year = models.BigIntegerField( blank=True, null=True)
    count = models.BigIntegerField()
    origin_city = models.TextField( blank=True, null=True)  # Field name made lowercase.
    destination_city = models.TextField( blank=True, null=True)  # Field name made lowercase.
    airline = models.TextField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flightroute'


class Monthlyflight(models.Model):
    month = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    count = models.BigIntegerField( blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type = models.TextField(blank=True, null=True)
    origin_country = models.TextField(blank=True, null=True)
    origin_region = models.TextField(blank=True, null=True)
    airline = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthlyflight'

class Airport(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField( blank=True, null=True)  # Field name made lowercase.
    city = models.TextField( blank=True, null=True)  # Field name made lowercase.
    country = models.TextField( blank=True, null=True)  # Field name made lowercase.
    icao = models.TextField( blank=True, null=True)  # Field name made lowercase.
    iata = models.TextField( blank=True, null=True)  # Field name made lowercase.
    keywords = models.TextField( blank=True, null=True)  # Field name made lowercase.
    region = models.TextField( blank=True, null=True)  # Field name made lowercase.
    continent = models.TextField( blank=True, null=True)  # Field name made lowercase.
    elevation_ft = models.DecimalField( blank=True, null=True, decimal_places=2, max_digits=10)  # Field name made lowercase.
    latitude_deg = models.DecimalField( blank=True, null=True, decimal_places=2, max_digits=10)  # Field name made lowercase.
    longitude_deg_ft = models.DecimalField( blank=True, null=True, decimal_places=2, max_digits=10)  # Field name made lowercase.
    type = models.TextField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'airport'