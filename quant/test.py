#!/usr/bin/python


import ReadCSVFile
import BacktestPair

data=[]
#data=ReadCSVFile.ReadCSVFile(dbpath='database/Banks/AbsaNed.csv')
data=ReadCSVFile.ReadCSVFile(dbpath='database/FullList/Investec.csv')

startDate=data[0]['TradeDate']
endDate=data[-1]['TradeDate']

a=BacktestPair.BacktestPair(pairData=data,startDate=startDate,endDate=endDate,generateReport=True,Spreads=[],adfTest=False)

