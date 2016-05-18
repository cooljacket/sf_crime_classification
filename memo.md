[5/18 00:35]
试了svm均匀采样，但是目测是support vector缺失，效果不是很好，2.5多
高神说xgboost很不错，可以轻松到2.3+
尝试多个模型来做，然后加起来，归一化（SVM，Random forest，else？）


[3/14 01:28]
早上起来记得写一个baseline的程序，跑结果后交上去，C++就好啦


[The best]
model = RandomForestClassifier(n_jobs=-1, max_depth=10, n_estimators=10, warm_start=True)
2.51068

[new way]
gradient boosting decision tree

