#!/usr/bin/python


def GenerateRowValue(begin='',end='',Spreads=[],csvData='',debug=False):
	from numpy import std,mean
	average=mean(Spreads[begin:end])
	stdev=std(Spreads[begin:end])
	csvData[end]['mean']=average
	csvData[end]['stdev']=stdev
	csvData[end]['zScore']=(Spreads[end]-average)/stdev
	return csvData

def main():
    adf=GenerateRowValue()

if __name__ == '__main__':
    main()

