#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void output(fstream& out, const vector<double>& data);


int main() {
	int size, row_size;
	fstream in("data/train_data.txt", ios::in);
	in >> size >> row_size;
	++row_size;

	vector<vector<double> > data(size, vector<double>(row_size));
	for (int i = 0; i < size; ++i)
		for (int j = 0; j < row_size; ++j)
			in >> data[i][j];

	in.close();
	random_shuffle(data.begin(), data.end());
	fstream out("data/train_data_rs.txt", ios::out);
	size /= 200;
	out << size << '\n' << row_size-1 << endl;
	for (int i = 0; i < size; ++i)
		output(out, data[i]);

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