import csv
import os

f = open("videos.csv")
csv_f = csv.reader(f)

for row in csv_f:
    print ""
    print ""
    print row[0]
    os.system("python2 vimeo-download.py --url "+row[1]+" --output "+row[0])