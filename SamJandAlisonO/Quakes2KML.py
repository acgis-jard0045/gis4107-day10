# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import os
def main():
    pass

def exportToKml(inFile, outKml):
    script_folder = "D:\\acgis\\gis4107_Intro2Prog\\day10\\lab\\SamJandAlisonO\\data"
    os.chdir(script_folder)
    with open(inFile, "r") as dataIn, open(outKml,"w") as dataOut:
        lineList = dataIn.readlines()
        dataOut.write(getKmlHeader())
        for line in lineList[1:]:

            line = line.rstrip()
            line = line.split(',')
            lat = line[1]
            lon = line[2]
            depth = line[3]
            mag = line[4]
            dataOut.write(getKmlPlacemark(lon, lat, depth, mag))
        dataOut.write(getKmlFooter())


def getKmlHeader():

    return """<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>"""



def getKmlPlacemark(longitude,latitude,depth,magnitude):
    magnitude=str(magnitude)
    depth=str(depth)
    longitude=str(longitude)
    latitude=str(latitude)
    return "\n<Placemark>\n<name>"+magnitude+"</name>\n<description>Mag="+magnitude+", Depth="+depth+" km</description>\n<Point>\n<coordinates>"+longitude+","+latitude+",0</coordinates>\n</Point>\n</Placemark>\n"




def getKmlFooter():
    return """</Document>\n</kml>\n"""



if __name__ == '__main__':
    main()