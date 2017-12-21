#!/usr/bin/python

def AddColumns(csvData):
	for i,row in enumerate(csvData):
		row.update( {
					'spread':0,
					'adfTest':0, 
					'mean':0, 
					'stdev':0,
					'zScore':0,
					'signal':0,
					'BuyPrice':0,
					'SellPrice':0,
					'LongReturn':0,
					'ShortReturn':0,
					'Slippage':0,
					'TotalReturn':0,
					'TransactionRatio':0,
					'TradeClose':0
				} )
	csvData[i]=row
	return csvData
				
def DisplayCSVData(data=''):
	from pprint import pprint
	pprint(data)

def main():
	csvData=[]
	csvData=AddColumns(csvData)
	DisplayCSVData(csvData)


if __name__ == '__main__':
	main()

