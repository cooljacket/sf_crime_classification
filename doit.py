from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def loadDataHelper(fileName):
	x = []
	y = []
	with open(fileName, 'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			line = line.split(',')
			y.append(int(line[0]))
			size = len(line)
			tmp_x = range(1, size)
			for i in range(1, size):
				# if size-i <= 2:
				# 	tmp_x[i-1] = float(line[i])
				# else:
				# 	tmp_x[i-1] = int(line[i])
				tmp_x[i-1] = float(line[i])
			x.append(tmp_x)
			# if len(x) >= 1000:
			# 	break

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


if __name__ == '__main__':
	# get X and y
	train_x, train_y = loadDataHelper('data/train_data.txt')
	test_x, test_id = loadDataHelper('data/test_data.txt')

	# fit a SVM model to the data
	# model = SVC()
	# model = LogisticRegression()
	# model = GaussianNB()
	# model = KNeighborsClassifier()
	# fit a CART model to the data
	# model = DecisionTreeClassifier()
	model = LinearSVC()
	model.fit(train_x, train_y)
	print(model)

	# make predictions
	# expected = train_y
	# predicted = model.predict(train_x)
	# # summarize the fit of the model
	# print(metrics.classification_report(expected, predicted))
	# print(metrics.confusion_matrix(expected, predicted))

	predicted = model.predict(test_x)
	saveResult('result-linearsvm.csv', test_id, predicted)
