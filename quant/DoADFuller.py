#!/usr/bin/python


def DoADFuller(csvData=''):
	import statsmodels.tsa.stattools as ts
	return ts.adfuller(csvData, 1)


def main():
	adf=0
	csvData=[]
	adf=DoADFuller(csvData=csvData)

if __name__ == '__main__':
	main()
