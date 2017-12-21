#!/usr/bin/python

def PrepareData(csvData='', debug=False):
	from AddColumns import AddColumns
	for i,row in enumerate(csvData):
		row.update( {'pairRatio':round(float(row['Sym1Close'])/float(row['Sym2Close']),6)})
		csvData[i]= row
		if debug: print csvData[i]

	csvData=AddColumns(csvData)
	return csvData

def DisplayCSVData(data=''):
	from pprint import pprint
	pprint(data)

def main():
	csvData=[]
	csvData=PrepareData(csvData)
	DisplayCSVData(csvData)

if __name__ == '__main__':
	main()
