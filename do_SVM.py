#encoding:utf-8
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.externals import joblib
import utils
import time


if __name__ == '__main__':
	start = time.time()
	# get X and y, the return data is all numpy 2d array
	train_x, train_y = utils.loadDataHelper('data/train_data_rs.txt')
	test_x, test_id = utils.loadDataHelper('data/test_data.txt')
	# test_x = test_x[0:3000:]
	print('train size: %d %d' % (len(train_x), len(train_y)))
	print('test size: %d %d' % (len(test_x), len(test_id)))

	#normalize the data attributes
	train_x = preprocessing.scale(train_x)
	test_x = preprocessing.scale(test_x)

	utils.display(train_x)
	print('begin')

	model = SVC(probability=True)
	model.fit(train_x, train_y)

	print('Training time {0}'.format(time.time() - start))
	print(model)

	# probs = model.predict_proba(test_x)
	utils.predict_and_save(test_x, model, 'results/result_SVM_nolog.csv', blockSize=50000)
	print('Total time {0}'.format(time.time() - start))