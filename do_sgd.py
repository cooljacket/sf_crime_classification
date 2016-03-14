#encoding:utf-8
from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import utils



if __name__ == '__main__':
	# get X and y, the return data is all numpy 2d array
	train_x, train_y = utils.loadDataHelper('data/train_data.txt')
	test_x, test_id = utils.loadDataHelper('data/test_data.txt')
	print('train size: %d %d' % (len(train_x), len(train_y)))
	print('test size: %d %d' % (len(test_x), len(test_id)))

	utils.display(train_x)

	# normalize the data attributes
	utils.Min_Max_Norm(train_x)
	utils.Min_Max_Norm(test_x)

	utils.display(train_x)
	print('begin')

	model = SGDClassifier(loss='log', alpha=0.01, n_jobs=2, n_iter=20)
	model.fit(train_x, train_y)
	print(model)

	probs = model.predict_proba(test_x)
	utils.saveResult('results/result_sgd.csv', probs)

# refer: http://scikit-learn.org/stable/modules/ensemble.html