#!/usr/bin/env python
#
# Converts gpsxml files to csv

import csv
import os
import re
import sys

if len(sys.argv) == 1:
    print "Usage: " + sys.argv[0] + " <GPSXML file>"
    exit()

filename = sys.argv[1]

# Open the input and output files
with open(filename, 'r') as inFile, open(filename.rsplit(".", 1)[0] + '.csv', 'w') as outFile:

    # Create CSV writer and write header
    writer = csv.writer(outFile)
    writer.writerow(['bssid','source','time-sec','time-usec','lat','lon','spd','heading','fix','alt','signal_dbm','noise_dbm'])

    # Parse the input
    for line in inFile:

        # We are only interested in data lines which all contain "gps-point"
        # Valid lines have either 9, 10, or 12 matches depending on
        # whether they contain "source", "sigal_dbm", and "noise_dbm"
        if "gps-point" in line:

            # Match everything in double quotes
            matches = re.findall(r'"(.*?)"', line)

            # Insert an empty string 'source'
            if len(matches) == 9:
                matches.insert(1,'')

            # Insert empty strings 'signal_dbm' and 'noise_dbm'
            if len(matches) == 9 or len(matches) == 10:
                matches.extend(['',''])

            writer.writerow(matches)
