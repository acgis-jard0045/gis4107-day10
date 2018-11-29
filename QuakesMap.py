import zipfile
import os
def main():
    exportToKmz()
    test_exportToKmz()



def exportToKmz():

    script_folder = "D:\acgis\gis4107_Intro2Prog\day10\lab\SamJandAlisonO"
    Kml = os.path.join(script_folder,"quakes2000.kml")

    print Kml
    print 'creating archive'
    zf = zipfile.ZipFile('zipfile_write.zip', mode='w')
    try:
        print 'adding README.txt'
        zf.write(Kml)
    finally:
        print 'closing'
        zf.close()




def test_exportToKmz():
    import zipfile

with zipfile.ZipFile("zipfile_write.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")
    outKml = os.path.join(script_folder,"quakes2000.kml")
    os.system("start " + "D:\acgis\gis4107_Intro2Prog\day10\lab\SamJandAlisonO\\targetdir\\D:\acgis\gis4107_Intro2Prog\day10\lab\SamJandAlisonO\\data\\quakes2000.kml")


if __name__ == '__main__':
    main()