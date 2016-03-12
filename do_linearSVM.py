#encoding:utf-8
from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import utils



if __name__ == '__main__':
	# get X and y
	train_x, train_y = utils.loadDataHelper('train_data.txt')
	test_x, test_id = utils.loadDataHelper('test_data.txt')
	print('train size: %d %d' % (len(train_x), len(train_y)))
	print('test size: %d %d' % (len(test_x), len(test_id)))

	utils.display(train_x)

	#normalize the data attributes
	train_x = preprocessing.scale(train_x)
	test_x = preprocessing.scale(test_x)

	utils.display(train_x)

	model = LinearSVC()
	model.fit(train_x, train_y)
	print(model)

	predicted = model.predict(test_x)
	utils.saveResult('result_linSVM.csv', test_id, predicted)
