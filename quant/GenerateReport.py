#!/usr/bin/python


def GenerateReport(csvData=[],startDate='',endDate=''):
	total=0
	for i,row in enumerate(csvData):
		if row['TotalReturn'] != 0:
			total=total+float(row['TotalReturn'])
			print i, row['TotalReturn'], total
	

def main():
	GenerateReport()

if __name__ == '__main__':
	main()

