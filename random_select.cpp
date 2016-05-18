#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <ctime>
#include <cstdlib>
using namespace std;

void output(fstream& out, const vector<double>& data);

typedef vector<vector<double> > Matrix;

const int MAX = 9997;
inline double Rand() {
	return (rand() % MAX) * 1.0 / MAX;
}


int main() {
	int size, row_size, type;
	fstream in("data/train_data.txt", ios::in);
	in >> size >> row_size;

	map<int, Matrix> data;
	for (int i = 0; i < size; ++i) {
		in >> type;
		vector<double> row(row_size + 1);
		for (int j = 1; j <= row_size; ++j)
			in >> row[j];
		row[0] = type;
		data[type].push_back(row);
	}

	in.close();
	
	fstream out("data/train_data_rs.txt", ios::out);
	double p = 0.05;
	Matrix final;

	for (map<int, Matrix>::iterator it = data.begin(); it != data.end(); ++it) {
		Matrix& tmp = it->second;
		random_shuffle(tmp.begin(), tmp.end());
		int cnt = p * tmp.size();
		if (cnt <= 5)
			cnt = min(60, int(tmp.size()));
		for (int i = 0; i < cnt; ++i)
			final.push_back(tmp[i]);
		cout << "Select " << cnt << '/' << tmp.size() << " samples for class " << it->first << endl;
	}
	
	cout << "total " << final.size() << '\n' << row_size << endl;
	out << final.size() << '\n' << row_size << endl;
	for (int i = 0; i < final.size(); ++i)
		output(out, final[i]);
	out.close();

	return 0;
}


void output(fstream& out, const vector<double>& data) {
	out << int(data[0]);
	int len = data.size();
	for (int i = 1; i < len; ++i) {
		if (len-i <= 2)
			out << ' ' << data[i];
		else
			out << ' ' << int(data[i]);
	}
	out << '\n';
}