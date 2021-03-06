# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flight(models.Model):
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
    flight = models.CharField(db_column='Flight', max_length=6, blank=True, null=True)  # Field name made lowercase.
    from_airport = models.CharField(db_column='From_Airport', max_length=4, blank=True, null=True)  # Field name made lowercase.
    to_airport = models.CharField(db_column='To_Airport', max_length=4, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flightlist'


class Flightroute(models.Model):
    month = models.TextField(blank=True, null=True)
    count = models.BigIntegerField()
    origin_city = models.TextField(db_column='Origin_City', blank=True, null=True)  # Field name made lowercase.
    destination_city = models.TextField(db_column='Destination_City', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flightroute'


class Monthlyflight(models.Model):
    month = models.TextField(blank=True, null=True)
    total_flights = models.BigIntegerField(db_column='total_flights', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'monthlyflight'

class Airport(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    icao = models.TextField(db_column='ICAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'airport'