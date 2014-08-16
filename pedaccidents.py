# <! Python 2.7
# Bryce

# dependancies: pyshp 1.2.1: https://pypi.python.org/pypi/pyshp

import os
os.chdir("H:/Academic Projects/datathon/scripts")

import shapefile

dbf = open("H:/Academic Projects/datathon/data/pedestrian victims/PedVictimsKSI.dbf", "rb")
shp = open("H:/Academic Projects/datathon/data/pedestrian victims/PedVictimsKSI.shp", "rb")

shapefile = shapefile.Reader(shp=shp, dbf=dbf)


records = shapefile.records()
fields = shapefile.fields
shapes = shapefile.shapes()

#available fields
print fields

#total records
print("\nTotal incidents: "+ str(len(records))+"\n")



for i in range(0,len(records)):
    print records[i][15] #neighborhood
    print records[i][4] #year



