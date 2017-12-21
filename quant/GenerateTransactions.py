#!/usr/bin/python


def GenerateTransactions(currentSignal,prevSignal,end,csvData):

	'''
	In a pair trading strategy you need to go long one share and short the other
	and then reverse the transaction when you close
  
	First Leg of the trade (Set Long position)
	if there is no change in signal
	'''

	if ( currentSignal == 0 ) and ( prevSignal == 0 ):
		csvData[end]['BuyPrice']=0
		csvData[end]['TransactionRatio']=0
	elif ( currentSignal == prevSignal ):
		csvData[end]['BuyPrice']=csvData[end-1]['BuyPrice']
		csvData[end]['TransactionRatio']=csvData[end-1]['TransactionRatio']

	# If the signals point to a new trade -- Short B and Long A
	elif ( currentSignal == 1 ) and (currentSignal != prevSignal):
		csvData[end]['BuyPrice']=csvData[end]['Sym1Close']
	# Short A and Long B
	elif ( currentSignal == -1 ) and (currentSignal != prevSignal):
		csvData[end]['BuyPrice']=float(csvData[end]['Sym2Close'])*float(csvData[end]['pairRatio'])
		transactionPairRatio=csvData[end]['pairRatio']
		csvData[end]['TransactionRatio']=transactionPairRatio

	# Close trades
	elif (currentSignal==0) and (prevSignal==1):
		csvData[end]['BuyPrice']=csvData[end]['Sym1Close']
	elif (currentSignal==0) and (prevSignal==-1):
		csvData[end]['TransactionRatio']=csvData[end-1]['TransactionRatio']
		csvData[end]['BuyPrice']=float(csvData[end]['Sym2Close'])*float(csvData[end]['TransactionRatio'])

	# Second Leg of the trade (Set Short position)
	# Set Short Prices if there is no change in signal
	if ( currentSignal == 0 ) and ( prevSignal == 0):
		csvData[end]['SellPrice']=0
	elif ( currentSignal == prevSignal ):
		csvData[end]['SellPrice']=csvData[end-1]['SellPrice']

	# if the signals point to a new trade
	elif (currentSignal == 1 ) and ( currentSignal != prevSignal ):
		csvData[end]['SellPrice']=csvData[end]['Sym2Close']*csvData[end]['pairRatio']
		transactionPairRatio=csvData[end]['pairRatio']
		csvData[end]['TransactionRatio']=transactionPairRatio
	elif ( currentSignal == -1 ) and (currentSignal != prevSignal ):
		csvData[end]['SellPrice']=csvData[end]['Sym1Close']

	# Close Trades
	elif ( currentSignal == 0 ) and ( prevSignal == 1 ):
		csvData[end]['TransactionRatio']=csvData[end-1]['TransactionRatio']
		csvData[end]['SellPrice']=csvData[end]['Sym2Close']*csvData[end]['TransactionRatio']
	elif ( currentSignal == 0 ) and ( prevSignal == -1):
		csvData[end]['SellPrice']=csvData[end]['Sym1Close']

	return csvData
		

def main():
	GenerateTransactions()

if __name__ == '__main__':
    main()
