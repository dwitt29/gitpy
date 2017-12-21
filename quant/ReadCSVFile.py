#!/usr/bin/python

def ReadCSVFile(dbpath='', debug=False):
	import csv
	columns=[ "TradeDate", "Sym1Close", "Sym2Close" ]
	csvData=[]
	with open(dbpath,'rb') as csvfile:
		chunk=csv.reader(csvfile, delimiter=',')
		chunk.next()
		for row in chunk:
			csvData.append(dict(zip(columns,row)))
			if debug: print row
	return csvData

def DisplayCSVData(data=''):
	from pprint import pprint
	pprint(data)

def main():
	from argparse import ArgumentParser
	parser=ArgumentParser()
	parser.add_argument('--dbpath', dest='dbpath')
	args=parser.parse_args()
	csvData=[]
	csvData=ReadCSVFile(dbpath=args.dbpath)
	DisplayCSVData(data=csvData)

if __name__ == '__main__':
    main()
