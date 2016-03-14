# ex1
from sklearn.datasets import load_iris
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
from sklearn import svm


def cv_estimate(model, X, KF):
	k_fold = KFold(n = X.shape[0], n_folds = KF)
	all_score = 0
	for k, (train_index, test_index) in enumerate(k_fold):
		# print(X.shape, train_index, test_index)
		model.fit(X[train_index], y[train_index])
		score = model.score(X[test_index], y[test_index])
		print("[fold {0}], score: {1:.5f}".format(k, score))
		all_score += score
	return all_score / KF


iris = load_iris()
X = iris.data
y = iris.target

K = 6
# model = LogisticRegression()
# svm
model = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print('{0}-fold validation rate is {1:.5f}'.format(K, cv_estimate(model, X, K)))


# ex2
from sklearn.datasets import load_iris
from sklearn.cross_validation import KFold
from sklearn import svm


iris = load_iris()
X = iris.data
y = iris.target

K = 6
model = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
scores = cross_validation.cross_val_score(model, X, y, cv=K)
print(scores)


# ex3
from sklearn.datasets import load_iris
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
from sklearn import svm

iris = load_iris()
X = iris.data
y = iris.target

model = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=233)
model.fit(X_train, y_train)
prob = model.predict_proba(X_test)
prob

model = LogisticRegression()
model.fit(X_train, y_train)
prob = model.predict_proba(X_test)
prob