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
reload (os)

def main():
    pass


script_folder = os.path.dirname(os.path.abspath(__file__))


def getFileContent(fileName):

    try:
        inFile = open(fileName)
        inText =inFile.read()

        return inText
    except:
        return fileName + "does not exist"

    pass

#def writeToFile (fileName, content):

#    with open(newFile,'w+') as f:
#        f.write('This is a new file')


def writeToFile (fileName, content):


    saveFile = open(fileName, 'w')

    saveFile.write(content)
    saveFile.close()

    f = open((os.path.join(script_folder, fileName)), 'r') # this opens the file in read mode

    contents = f.read() # this reads the contents of the file

    return  contents

    pass


if __name__ == '__main__':
    main()