import xml.etree.ElementTree as ET
import csv

NS = 'http://www.tei-c.org/ns/1.0'
with open('nileMeasure.csv', 'w') as f:
	writer = csv.writer(f)
	tree = ET.parse('nileMeasure.xml')
	root = tree.getroot()
	for row in root.iterfind('.//{%s}row' % NS ):
		data = []
		for cell in row.iterfind('./{%s}cell' % NS ):
			data.append(cell.text)
		writer.writerow(data)