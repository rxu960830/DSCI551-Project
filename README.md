# DSCI551-Project
This is the github page for AWS data project by Ruojia

This project include 3 parts:

A) A PySpark data tranformation jupyter notebook running on spark-notebook Docker hosted on aws EC2 (IaaS);
B) A Django server to manage and view transformed "Flights" datasets, hosted on EC2 (IaaS) + aws RDS with PostgreSQL DB (PaaS);
C) A Dashboard using aws QuickSights (SaaS) to visulize and analyze transformed "Flights" data.



Part A)
Data Transformation using PySpark.
The raw data include:
1. OpenSky Network Flights data. https://zenodo.org/record/6411336#.YkrpZS-l1-U
2. ICAO airports master data. https://davidmegginson.github.io/ourairports-data/airports.csv

Total 7,301,152 flight records / 71850 airport records after cleaning.

OpenSky Network Flights dat: Origin and destination airports are computed online based on the ADS-B trajectories on approach/takeoff: no crosschecking with external sources of data has been conducted.
Fields origin or destination are empty when no airport could be found.
Aircraft information come from the OpenSky aircraft database. Fields typecode and registration are empty when the aircraft is not present in the database.
Description of the dataset

One file per month is provided as a csv file with the following features:

callsign: the identifier of the flight displayed on ATC screens (usually the first three letters are reserved for an airline: AFR for Air France, DLH for Lufthansa, etc.)
number: the commercial number of the flight, when available (the matching with the callsign comes from public open API)
icao24: the transponder unique identification number;
registration: the aircraft tail number (when available);
typecode: the aircraft model type (when available);
origin: a four letter code for the origin airport of the flight (when available);
destination: a four letter code for the destination airport of the flight (when available);
firstseen: the UTC timestamp of the first message received by the OpenSky Network;
lastseen: the UTC timestamp of the last message received by the OpenSky Network;
day: the UTC day of the last message received by the OpenSky Network;
latitude_1, longitude_1, altitude_1: the first detected position of the aircraft;
latitude_2, longitude_2, altitude_2: the last detected position of the aircraft.

Part B)
Data Management and Access using Django.
To run the Django server:
1. clone the respository: 
  git clone https://github.com/rxu960830/DSCI551-Project.git
2. go to the main directory:
  cd citysearch_project
3. start django server:
  python3 manage.py runserver 0.0.0.0:8000

Part C)
Data Visulization and Analysis using QuickSight.
https://ap-northeast-1.quicksight.aws.amazon.com/sn/start/analyses
