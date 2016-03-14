#include <fstream>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <assert.h>
#include <sstream>
#include <iomanip>
using namespace std;

const string CATEGORIES_String = "Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS";
const int TrainDataSize = 878049, TestDataSize = 884262, Row_size = 8;

vector<string> splite(const string& s);
void readTrainData(const char* outFileName);
map<string, int> Categories;


int main() {
	readTrainData("results/baseline.csv");
	return 0;
}

vector<string> splite(const string& s) {
	vector<string> vs;
	string buf(s.size(), ' ');
	int len = 0, end = s.size() - 1;
	int quote_cnt = 0;
	for (int i = 0; i <= end; ++i) {
		if (s[i] != ',')
				buf[len++] = s[i];
		if (s[i] == '"') {
			++quote_cnt;
			if (quote_cnt >= 2)
				quote_cnt = 0;
		}

		if ((s[i] == ',' && quote_cnt == 0) || i == end) {
			vs.push_back(buf.substr(0, len));
			len = 0;
		}
	}

	return vs;
}


void readTrainData(const char* outFileName) {
	fstream data("data/train.csv", ios::in);
	fstream out(outFileName, ios::out);
	string line;
	getline(data, line);	// ignore the header line

	while (getline(data, line)) {
		vector<string> vs = splite(line);
		++Categories[vs[1]];
	}

	out << CATEGORIES_String << endl;
	vector<string> vs = splite(CATEGORIES_String);
	for (int i = 0; i < TestDataSize; ++i) {
		out << i;
		for (int j = 1; j < vs.size(); ++j)
			out << ',' << Categories[vs[j]] * 1.0 / TestDataSize;
		out << '\n';
	}

	out.close();
	data.close();
}