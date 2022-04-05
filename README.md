# DSCI551-Project
This is the github page for AWS data project by Ruojia

This project include 3 parts:

A) A PySpark data tranformation jupyter notebook running on spark-notebook Docker hosted on aws EC2
B) A Django server to manage and view transformed "Flights" datasets, hosted on EC2 (IaaS) + aws RDS with PostgreSQL DB (PaaS)
C) A Dashboard using aws QuickSights (SaaS) to visulize and analyze transformed "Flights" data



Part A)
Data Transformation using PySpark


Part B)
Data Management and Access using Django
To run the Django server:
1. clone the respository: 
  git clone https://github.com/rxu960830/DSCI551-Project.git
2. go to the main directory:
  cd citysearch_project
3. start django server:
  python3 manage.py runserver 0.0.0.0:8000

Part C)
Data Visulization and Analysis using QuickSight
