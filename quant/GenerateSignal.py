#!/usr/bin/python



def GenerateSignal(counter=0,csvData=[]):
	# Trigger and Close represent the entry and exit zones (value refers to zscore value)
	trigger=1
	close=0.5

	currentSignal=csvData[counter]['signal']
	prevSignal=csvData[counter-1]['signal']

	if ( csvData[counter]['adfTest'] == 1):
		# If there is a change in signal from long to short then you must allow for the 
		# current trade to first be closed
		if ( currentSignal == -1 ) and (prevSignal == 1):
			csvData[counter]['signal']=0
		elif ( currentSignal == 1 ) and ( prevSignal == -1 ):
			csvData[counter]['signal']=0

		# Create a long / short signal if the current z-score is larger / smaller than the trigger value(respectively)
		elif ( csvData[counter]['zScore'] > trigger ):
			csvData[counter]['signal'] = -1
		elif ( csvData[counter]['zScore'] < -trigger ):
			csvData[counter]['signal'] = -1

		# Close the position if z-score is beteween the two "close" values
		elif ( csvData[counter]['zScore'] < close ) and ( csvData[counter]['zScore'] > -close ):
			csvData[counter]['signal']=0
		else:
			csvData[counter]['signal']=prevSignal

	else:
		csvData[counter]['signal']=0

	return csvData

			

		
	

def main():
    GenerateSignal()


if __name__ == '__main__':
    main()

