#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     02/10/2018
#-------------------------------------------------------------------------------

import csv
import string
import os
reload(os)

script_folder = os.path.dirname(os.path.abspath(__file__))
in_csv = open(os.path.join(script_folder, "Haiti_Admin_Names.csv"), 'r')
out_csv = open(os.path.join(script_folder, "Fixed_Haiti_Admin_Names.csv"), 'w')
admin_code_column_index = 0

def process_file():
    data = csv.reader(in_csv)

    for line in data:
        line = str(line)
        new_line = str.replace(line,specials,'')
        writer.writerow(new_line.split(','))

    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    input_file.close()
    output_file.close()


pass


def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""

    pass

























