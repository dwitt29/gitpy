#!/usr/bin/python

def BacktestPair(pairData='', mean=35, slippage=-0.0025, adfTest=True, criticalValue=-2.58, startDate='',endDate='',generateReport=False, Spreads=[]):

# At 150 data points
# Critical value at 1% : -3.46
# Critical value at 5% : -2.88
# Critical value at 10% : -2.57

	from DoADFuller import DoADFuller
	from PrepareData import PrepareData
	from GenerateRowValue import GenerateRowValue
	from GenerateSignal import GenerateSignal
	from GenerateTransactions import GenerateTransactions
	from GetReturnsDaily import GetReturnsDaily
	from GenerateReport import GenerateReport
	pairData=PrepareData(csvData=pairData)

	#Iterate through each day in the time series
	for i,row in enumerate(pairData):
		begin=i-mean+1
		end=i

		#Calculate Spread
		spread=pairData[end]['pairRatio']
		pairData[end]['spread']=spread		
		print int(end),float(spread),type(Spreads),len(Spreads)
#		Spreads[int(end)]=float(spread)
		Spreads.append(float(spread))

		if (i >= mean):
			#Generate Row Values
			pairData=GenerateRowValue(begin=begin, end=end, Spreads=Spreads, csvData=pairData)
	
		#For each day after the amount of days needed to run the ADF test
		if (i > 130):

			#ADF Test 
			#120 - 90 - 60 
			if (adfTest == False):
				pairData[end]['adftest']=1
			else:
				if(DoADFuller(csvData=Spreads[i-120:end])[0] <= criticalValue):
					if(DoADFuller(csvData=Spreads[i-90:end])[0] <= criticalValue):
						if(DoADFuller(csvData=Spreads[i-60:end])[0] <= criticalValue):
							pairData[end]['adfTest']=1

			# Generate Signals
			pairData=GenerateSignal(counter=i,csvData=pairData)
	
			currentSignal = pairData[i]['signal']
			prevSignal = pairData[i-1]['signal']

			# Generate Transactions
			pairData = GenerateTransactions(currentSignal=currentSignal, prevSignal=prevSignal, end=i, csvData=pairData)

			# Get the returns with added slippage
			pairData = GetReturnsDaily(i, pairData,slippage)

	if ( generateReport == True ):
		GenerateReport(csvData=pairData,startDate=startDate,endDate=endDate)

	return pairData

def main():
	BacktestPair()


if __name__ == '__main__':
    main()

