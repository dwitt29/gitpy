#!/usr/bin/python

# Calculate daily returns generated 
# Add implementation shortfall / slippage at close of trade

def GetReturnsDaily(end=0,csvData=[],slippage=0):
	from math import log
	# Calculate the returns generated on each leg of the deal (the long and the short position)
	# Long leg of the trade
	if ( csvData[end-1]['signal'] > 0 ):
		csvData[end]['LongReturn'] = log(csvData[end]['Sym1Close'] / csvData[end-1]['Sym1Close'])
	elif ( csvData[end-1]['signal'] < 0 ):
		csvData[end]['LongReturn'] = log(float(csvData[end]['Sym2Close']) / float(csvData[end-1]['Sym2Close']))*csvData[end]['TransactionRatio']

	# Short leg of the trade
	if ( csvData[end-1]['signal'] > 0 ):
		csvData[end]['ShortReturn'] = -log(csvData[end]['Sym2Close'] / csvData[end-1]['Sym2Close'])*csvData[end]['TransactionRatio']
	elif ( csvData[end-1]['signal'] < 0 ):
		csvData[end]['ShortReturn'] = -log(float(csvData[end]['Sym1Close']) / float(csvData[end-1]['Sym1Close']))

	# add slippage
	if ( csvData[end]['signal'] == 0 ) and (csvData[end-1]['signal'] != 0 ):
		csvData[end]['Slippage']=slippage
		csvData[end]['TradeClose']=1

	#If a trade was closed then calculate the total return
	csvData[end]['TotalReturn']= ((csvData[end]['ShortReturn']+csvData[end]['LongReturn'])/2)+csvData[end]['Slippage']

	return csvData

def main():
    GetReturnsDaily()


if __name__ == '__main__':
    main()

