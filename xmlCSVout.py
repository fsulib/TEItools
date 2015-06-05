import xml.etree.ElementTree as ET
import csv
import sys

def writeCSV(fileIn, fileOut):
#	print(fileIn)
#	print(fileOut)
	NS = 'http://www.tei-c.org/ns/1.0'
	with open(fileOut, 'w') as f:
		writer = csv.writer(f)
		tree = ET.parse(fileIn)
		root = tree.getroot()
		for row in root.iterfind('.//{%s}row' % NS ):
			data = []
			for cell in row.iterfind('./{%s}cell' % NS ):
				data.append(cell.text)
			writer.writerow(data)

fileIn = sys.argv[1]
fileOut = sys.argv[2]
writeCSV(fileIn, fileOut)
