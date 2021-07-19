#!/usr/bin/python

import csv

f = open('crawled.csv', 'r')

reader = csv.DictReader(f,fieldnames=['im','dos', 'date','time','url'])
next(reader)

w = open('domestic.csv', 'w')
writer = csv.writer(w,quotechar='"')
writer.writerow(['date', 'province','number','time','url'])
import re
for row in reader:
    if row['dos'] == "":
        continue
    res1 = re.findall(r'(?:(?:,|(?:tại)):?\s*([^\d\(]+) \((\s?\d+(?:\.\d+)?\s?)\))', row['dos'], re.IGNORECASE)
    # res1 = re.findall(r'(?:trong nước|trong nước) (?:tại|tại):?\s*([^\d\(]+) \((\s?\d+(?:\.\d+)?\s?)\)', row['dos'], re.IGNORECASE)

    if res1:
        for x in res1:
            writer.writerow([row['date'], x[0],x[1], row['time'],row['url']])
        pass
    else:
        print(row['time'], row['dos'])

w.close()