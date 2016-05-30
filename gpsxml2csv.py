#!/usr/bin/env python
#
# Converts gpsxml files to csv

import sys
import re
import csv

# Get filename to parse from command line
filename = sys.argv[1]

# Open the input and output files
with open(filename, 'r') as inFile, open('parsed.csv', 'w') as outFile:

    # Create CSV writer and write header
    writer = csv.writer(outFile)
    writer.writerow(['bssid','time-sec','time-usec','lat','lon','spd','heading','fix','alt'])

    # Parse the input
    for line in inFile:

        # We are only interested in data lines which all contain "gps-point"
        if "gps-point" in line:

            # Match everything in double quotes
            matches = re.findall(r'"(.*?)"', string)

            # Valid lines have either 9 or 11 matches
            if len(matches) == 9:
                wrtier.writerow(matches)

            if len(matches) == 11:
                del matches[1]
                writer.writerow(matches[0:9])

