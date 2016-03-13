<meta charset="utf8">
# 代码结构
- trans_data.cpp	将原始csv格式转化为需要的文本数据
- do_xxx.py		后面跟着的是所用的算法的简写，每个基本都是一样的，只是所用的模型不一样而已
- utils.py		是自己写的读入数据、写出结果、展示数据的工具库


# 思路发展的说明
1. 数据预处理
首先是将原始数据（record格式，即有很多是字符串的描述）转化为data matrix格式（即全部为数据的格式），具体的转换放在在trans_data.cpp中有描述清楚。


2. 特征的选择
这部分是最重要部分之一（另外一部分是选择合适的模型和参数），训练数据和测试数据共有的特征有:
	* 1）Dates；
	* 2）DayOfWeek；
	* 3）PdDistrict；
	* 4）X（Longitude）；
	* 5）Y（Latitude）。
所以只能在这五个维度的基础上来做。

具体怎么做呢？应该需要用到“特征工程”的一些知识（待讨论，参考：https://www.zhihu.com/question/28641663）。


# 现在正在做的事
我现在正在尝试用合理的方法将数据归一化，再跑一遍试试看结果


# 需要大家做的事
- 1）学会用scikit-learn库或者别的库，来做相关性分析；
- 2）看一下如何选取特征比较好，模型方面可以暂时我来写就好了，等到后面有教再大家一起做。


