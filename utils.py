#encoding:utf-8
import numpy as np

def loadDataHelper(fileName):
	with open(fileName, 'r') as f:
		row_size = int(f.readline())
		col_size = int(f.readline())
		x = np.zeros([row_size, col_size])
		y = np.arange(row_size)
		index = 0
		print(row_size, col_size, index)

		while True:
			line = f.readline()
			if not line:
				break
			line = line.split(',')
			y[index] = int(line[0])
			size = len(line)
			tmp_x = range(1, size)
			for i in range(1, size):
				# if size-i <= 2:
				# 	tmp_x[i-1] = float(line[i])
				# else:
				# 	tmp_x[i-1] = int(line[i])
				x[index][i-1] = float(line[i])
			index += 1

	return (x, y)


def saveResult(fileName, ids, labels):
	with open(fileName, 'w') as f:
		header =  "Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS\n"
		f.write(header)
		size = header.count(',')
		for (id, label) in zip(ids, labels):
			f.write('%d' % int(id))
			for i in range(0, size):
				if i == label:
					f.write(',1')
				else:
					f.write(',0')
			f.write('\n')


def display(x):
	for i in range(0, 10):
		print(x[i])
