#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv
import sys
import os

def writeCSV(fileName):
	NS = 'http://www.tei-c.org/ns/1.0'
	with open(fileName + '.csv', 'w') as f:
		writer = csv.writer(f)
		tree = ET.parse(fileName + '.xml')
		root = tree.getroot()
		for row in root.iterfind('.//{%s}row' % NS ):
			data = []
			for cell in row.iterfind('./{%s}cell' % NS ):
				data.append(cell.text)
			writer.writerow(data)

name = os.path.splitext(sys.argv[1])[0]
writeCSV(name)
