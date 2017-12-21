#!/usr/bin/python


# https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing

#import pandas_datareader as pdr
#from datetime import datetime
#import statsmodels.tsa.stattools as ts
#goog=pdr.get_data_yahoo('GOOG',datetime(2000,1,1), datetime(2013,1,1))
#print ts.adfuller(goog['Adj Close'], 1)
#pandas.date_range(datetime(2000,1,1), datetime(2013,1,1))

from datetime import datetime, timedelta
from math import log10, log
from pprint import pprint
import sys

def GetData(symbol,sdate,edate):
   import pandas_datareader as pdr
   return pdr.get_data_yahoo(symbol, sdate, edate)

#def DoADFuller(data):
#    import statsmodels.tsa.stattools as ts
#    return ts.adfuller(data['Close'], 1)

def DoADFuller(data):
    import statsmodels.tsa.stattools as ts
    return ts.adfuller(data, 1)

def BackTestPair(	data=[], mean=35, 
					slippage = -0.0025, adfTest = True, 
					criticalValue = -2.58, startDate = '2005-01-01', 
					endDate = '2014-11-23', generateReport = True, Spreads=[], debug=False	):

	for i,row in enumerate(data):
		begin=i - mean + 1
		end=i
		if i > 130:
			spread = data[end]['PairRatio']
			Spreads[int(end)]=spread
			data[end]['spread'] = spread
			if adfTest == False:
				data[end]['adfTest'] = 1
			else:
				if debug: print "\nOuter: adf=%f, crit=%f, i=%d, end=%d" % (DoADFuller(data=Spreads[i-120:end])[0],criticalValue,i-120,end)
				if ( DoADFuller(data=Spreads[i-120:end])[0] <= criticalValue ):
					if debug: print "Middle: adf=%f, crit=%f, i=%d, end=%d" % (DoADFuller(data=Spreads[i-90:end])[0],criticalValue,i-90,end)
					if ( DoADFuller(data=Spreads[i-90:end])[0] <= criticalValue ):
						if debug: print "Inner: adf=%f, crit=%f, i=%d, end=%d" % (DoADFuller(data=Spreads[i-60:end])[0],criticalValue,i-60,end)
						if ( DoADFuller(data=Spreads[i-60:end])[0] <= criticalValue ):
							data[end]['adfTest'] = 1
							if debug: pprint(data[end])
		if i >= mean:
			GenerateRowValue(begin=begin,end=end, Spreads=Spreads, data=data)
			GenerateSignal(counter=i, data=data, debug=False) 
			if debug: pprint(data[i]) 
			currentSignal=data[i]['signal']
			prevSignal=data[i-1]['signal']
			GenerateTransactions(currentSignal, prevSignal, i, data)
			GetReturns(end=i,data=data,slippage=slippage,debug=True)
				
	if (generateReport == True):
		#GenerateReport(data, startDate, EndDate)
		pprint(data) 
	return data


def GetReturns(end,data,slippage,debug=False):

	# Calculate the returns generated on each leg of the deal (the long and the short position)
	# Long Leg of the trade
	TotalProfit=0
	if ( data[end]['signal'] == 0 ) and ( data[end-1]['signal'] != 0 ):
		data[end]['LongReturn'] = log(data[end]['BuyPrice'] / data[end-1]['BuyPrice']) 
		if debug: print "Long Trade Return: end=%d, BP=%f, BP-1:%f, Profit=%f, Percent:%f" % (end,data[end]['BuyPrice'],data[end-1]['BuyPrice'],data[end]['BuyPrice']-data[end-1]['BuyPrice'],data[end]['LongReturn'])
	# Short Leg of trade
	if ( data[end]['signal'] == 0 ) and ( data[end-1]['signal'] != 0 ):
		data[end]['ShortReturn'] = log(data[end-1]['SellPrice'] / data[end]['SellPrice'])
		if debug: print "Short Trade Return: end=%d, SP-1=%f, SP:%f, Profit=%f, Percent:%f" % (end, data[end-1]['SellPrice'],data[end]['SellPrice'],data[end-1]['SellPrice']-data[end]['SellPrice'],data[end]['ShortReturn'])

	# Add slippage
	if ( data[end]['signal'] == 0 ) and ( data[end-1]['signal'] != 0 ): 
		data[end]['Slippage'] = slippage

	# if a trade was close then calculate the total return
	if ( data[end]['signal'] == 0 ) and ( data[end-1]['signal'] != 0 ):
		data[end]['TotalReturn'] = (( data[end]['ShortReturn'] + data[end]['LongReturn'])/2) + data[end]['Slippage'] 

	return data


def GenerateTransactions(currentSignal,prevSignal,end,data):
	# First leg of the trade (set long position), if there is no change in signal
	if (currentSignal == 0) and ( prevSignal == 0 ):
		data[end]['BuyPrice']=0
		data[end]['TransactionRatio']=0
	elif (currentSignal == prevSignal ):
		data[end]['BuyPrice']=data[end-1]['BuyPrice']
		data[end]['TransactionRatio']=data[end-1]['TransactionRatio']

	# if signals point to a new trade - ShortB and LongA
	elif ( currentSignal == 1) and ( currentSignal != prevSignal):
		data[end]['BuyPrice']=data[end]['Sym1TradeClose']
	# ShortA and LongB
	elif ( currentSignal == -1 ) and (currentSignal != prevSignal):
		data[end]['BuyPrice']=data[end]['Sym2TradeClose'] * data[end]['PairRatio']
		transactionPairRatio = data[end]['PairRatio']
		data[end]['TransactionRatio']=transactionPairRatio

	# Close trades
	elif ( currentSignal == 0) and ( prevSignal == 1 ):
		data[end]['BuyPrice']=data[end]['Sym1TradeClose']
	elif ( currentSignal == 0 ) and ( prevSignal == -1 ):
		data[end]['TransactionRatio']=data[end-1]['TransactionRatio']
		data[end]['BuyPrice']=data[end]['Sym2TradeClose']*data[end]['TransactionRatio']

	# Second Leg of the trade (set short position).  Set Short Prices if there is no change in signal

	if ( currentSignal == 0) and ( prevSignal == 0 ):
		data[end]['SellPrice'] = 0
	elif ( currentSignal == prevSignal ):
		data[end]['SellPrice'] = data[end-1]['SellPrice']
	# if the signals point to a new trade
	elif (currentSignal == 1) and ( currentSignal != prevSignal):
		data[end]['SellPrice']=data[end]['Sym2TradeClose'] * data[end]['PairRatio']
		transactionPairRatio = data[end]['PairRatio']
		data[end]['TransactionRatio']=transactionPairRatio
	elif ( currentSignal == -1 ) and ( currentSignal != prevSignal):
		data[end]['SellPrice']=data[end]['Sym1TradeClose']
	# close trades
	elif ( currentSignal == 0 ) and ( prevSignal == 1 ):
		data[end]['TransactionRatio']=data[end-1]['TransactionRatio']
		data[end]['SellPrice']=data[end]['Sym2TradeClose'] * data[end]['TransactionRatio']
	elif ( currentSignal == 0 ) and ( prevSignal == -1 ):
		data[end]['SellPrice']=data[end]['Sym1TradeClose']

	return data


def GenerateRowValue(begin, end, Spreads=[], data=[]):
	from numpy import std,mean
	stddev = std(Spreads[begin:end])
	mean = mean(Spreads[begin:end]) 
	data[end]['mean']=mean
	data[end]['stddev']=stddev
	data[end]['zScore']=(Spreads[end]-mean)/stddev
	
#	print "begin=%d, end=%d, stddev=%f, mean=%f" % (begin,end,stddev, mean)
#	print(Spreads[begin:end])
#	pprint(data[end])

def GenerateSignal(counter, data, debug=False):
	trigger=1
	close=0.5
	#pprint(data[counter])
	currentSignal=data[counter]['signal']
	prevSignal=data[counter-1]['signal']

	if data[counter]['adfTest']==1:
		if debug: print "counter=%d, adftest=%d" % (counter,data[counter]['adfTest'])
		# if there is a change in signal from long to short the nyou must allow for the current trade to first be closed
		if ( currentSignal == -1 ) and ( prevSignal == 1 ):
			data[counter]['signal'] = 0
			if debug: print "SIGNAL : counter=%d, currentSignal=%d, prevSignal=%d" % (counter, currentSignal, prevSignal)

		elif ( currentSignal == 1) and ( prevSignal == -1 ):
			data[counter]['signal'] = 0
			if debug: print "SIGNAL : counter=%d, currentSignal=%d, prevSignal=%d" % (counter, currentSignal, prevSignal)

		# create a long / short signal if the current zscore is larger / smaller than the trigger value (respectively)
		elif ( data[counter]['zScore'] > trigger):
			data[counter]['signal'] = -1
			if debug: print "zSCORE : counter=%d, currentSignal=%d, prevSignal=%d, zscore=%f > +trigger=%d" % (counter, currentSignal, prevSignal, data[counter]['zScore'], trigger)

		elif ( data[counter]['zScore'] < (-1*trigger) ):
			data[counter]['signal'] = 1
			if debug: print "zSCORE : counter=%d, currentSignal=%d, prevSignal=%d, zscore=%f < -trigger=%d" % (counter, currentSignal, prevSignal, data[counter]['zScore'], -1*trigger)

		# close the position if zscore is between the two "close" values
		elif ( data[counter]['zScore'] < close ) and ( data[counter]['zScore'] > (-1*close) ):
			data[counter]['signal']=0
			if debug: print "zSCORE : counter=%d, currentSignal=%d, prevSignal=%d, zscore=%f, close=%f" % (counter, currentSignal, prevSignal, data[counter]['zScore'], close)

		else:
			data[counter]['signal'] = prevSignal		
			if debug: print "SIGNAL : counter=%d, currentSignal=%d, prevSignal=%d, zscore=%f" % (counter, currentSignal, prevSignal, data[counter]['zScore'])
	else:
		data[counter]['signal']=0
		if debug: print "SIGNAL : counter=%d, adftest=%d" % (counter,data[counter]['adfTest'])

def main():
	csvData=[]
	Spreads=[]
	edate=datetime(2016,1,7); sdate=datetime(2005,1,1)
	Sym1='GS'; Sym2='CS'
	d1=GetData(Sym1, sdate, edate ); d2=GetData(Sym2, sdate, edate ) 
	dd1=d1.to_dict(); dd2=d2.to_dict()

	index=0
	# populate closing prices and initialize other fields
	for i in sorted(dd1['Close'].keys()):
		Sym1TradeClose=round(dd1['Close'][i],2)
		Sym2TradeClose=round(dd2['Close'][i],2)
		Spreads.append(0)
		csvData.append( {   'ArrayIndex':index,	
							'Symbol1':Sym1,
							'Symbol2':Sym2,
							'TradeDate':i,
							'Sym1TradeClose':Sym1TradeClose,
							'Sym2TradeClose':Sym2TradeClose,
							'PairRatio':round(Sym1TradeClose/Sym2TradeClose,6),
							#'Sym1Log10':round(log10(Sym1TradeClose),6),
							#'Sym2Log10':round(log10(Sym2TradeClose),6),
							'spread':0,
							'adfTest':0,
							'mean':0,
							'stddev':0,
							'zScore':0,
							'signal':0,
							'BuyPrice':0,
							'SellPrice':0,
							'LongReturn':0,
							'ShortReturn':0,
							'Slippage':0,
							'TransactionRatio':0,
							'TotalReturn':0 } )
		index+=1
	BackTestPair(data=csvData,startDate=sdate,endDate=edate,Spreads=Spreads, generateReport = False)
	#pprint(csvData[-10:])
	#pprint( Spreads[-10:])
	#adfSpreads=DoADFuller(Spreads)
	#pprint( adfSpreads)
	#pprint( adfSpreads[0])


if __name__ == '__main__':
    main()
