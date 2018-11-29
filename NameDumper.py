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
import glob
import sys

def main():
    pass


def dumpFileList(folder, dumpFile):
    if os.path.exists(folder):
        outFile= open(dumpFile,"w")
        os.chdir(folder)
        for file in glob.glob("two.txt"):
            os.chdir("D:\\acgis\\gis4107_Intro2Prog\\day10\\lab\\SamJandAlisonO\\TestFolder")
            print(file)
            outFile = open (dumpFile, "a")
            outFile.write(file +"\n")
        outFile.close()
    else:
        print "folder doesnt exist"
        sys.exit()

if __name__ == '__main__':
    main()