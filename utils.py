#encoding:utf-8
import numpy as np
import zipfile
from sklearn.externals import joblib



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
			line = line.split(' ')
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


# refer: http://python.jobbole.com/81519/
# ZIP_DEFLATED means that you want to compress it well into a smaller file
def CompressFile(fileName):
	zip = zipfile.ZipFile('{0}.zip'.format(fileName), 'w')
	zip.write(fileName, fileName, zipfile.ZIP_DEFLATED)
	zip.close()


def saveResultHelper(f, probs, start_id=0):
	id = start_id
	for p in probs:
		f.write('%d' % int(id))
		id += 1
		for pp in p:
			f.write(',{0:.3}'.format(pp))
		f.write('\n')


def saveResult(fileName, probs):
	with open(fileName, 'w') as f:
		header =  "Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS\n"
		f.write(header)
		saveResultHelper(f, probs, 0)
		
	CompressFile(fileName)


# I have to split the test data, because it cost too much memory...
def predict_and_save(test_x, model, resultFile, blockSize=5000):
	# first, load the model into memory
	# model = joblib.load(modelFile)

	# clear the old data
	with open(resultFile, 'w') as f:
		pass

	with open(resultFile, 'a') as f:
		# then predict each portion gradually
		for start_id in range(0, len(test_x), blockSize):
			probs = model.predict_proba(test_x[start_id:start_id+blockSize:])

			# finally, append the result to the result file
			if start_id == 0:
				header =  "Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS\n"
				f.write(header)
			saveResultHelper(f, probs, start_id)
			print('RF is dealing with {0}'.format(start_id))

	CompressFile(resultFile)


def display(x):
	for i in range(0, 10):
		print(x[i])


# x to be in range [-1, 1]
def Min_Max_Norm(x):
	max = np.max(x, axis=0)
	min = np.min(x, axis=0)
	x = (x-min) / (max-min)


# standardize
def Z_score_Norm(x):
	mean = x.mean(axis=0)
	std = x.std(axis=0)
	x = (x - mean) / std