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
    flight_number = models.TextField(blank=True, null=True)
    share_code = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight'


class Flightlist(models.Model):
    id = models.TextField(primary_key=True)
    flight = models.CharField( max_length=6, blank=True, null=True)  # Field name made lowercase.
    from_airport = models.CharField( max_length=4, blank=True, null=True)  # Field name made lowercase.
    to_airport = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flightlist'


class Flightroute(models.Model):
    id = models.TextField(primary_key=True)
    month = models.TextField(blank=True, null=True)
    count = models.BigIntegerField()
    origin_city = models.TextField( blank=True, null=True)  # Field name made lowercase.
    destination_city = models.TextField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flightroute'


class Monthlyflight(models.Model):
    month = models.TextField(blank=True, null=True)
    total_flights = models.BigIntegerField( blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'monthlyflight'

class Airport(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField( blank=True, null=True)  # Field name made lowercase.
    city = models.TextField( blank=True, null=True)  # Field name made lowercase.
    country = models.TextField( blank=True, null=True)  # Field name made lowercase.
    icao = models.TextField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'airport'