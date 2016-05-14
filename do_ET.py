#encoding:utf-8
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.externals import joblib
import utils



if __name__ == '__main__':
	# get X and y, the return data is all numpy 2d array
	train_x, train_y = utils.loadDataHelper('data/train_data.txt')
	test_x, test_id = utils.loadDataHelper('data/test_data.txt')
	# test_x = test_x[0:3000:]
	print('train size: %d %d' % (len(train_x), len(train_y)))
	print('test size: %d %d' % (len(test_x), len(test_id)))

	#normalize the data attributes
	train_x = preprocessing.scale(train_x)
	test_x = preprocessing.scale(test_x)

	# I found that it is better to use the above functions to dl normalization!!!
	# utils.Min_Max_Norm(train_x)
	# utils.Min_Max_Norm(test_x)
	utils.display(train_x)
	print('begin')

	model = ExtraTreesClassifier(n_jobs=-1, max_depth=15, n_estimators=200, warm_start=False)
	model.fit(train_x, train_y)
	print(model)

	utils.predict_and_save(test_x, model, 'results/result_ET.csv', blockSize=50000)