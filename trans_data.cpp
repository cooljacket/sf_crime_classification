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

const string CATEGORIES_String = "ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS";
const string DaysInAWeek[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
const int TrainDataSize = 878049, TestDataSize = 884262, Row_size = 8;

vector<string> splite(const string& s);
inline int str2int(const string& s);
inline double str2double(const string& s);
vector<int> time_to_int(const string& s);
int getPdDistrictId(const string& s);
void output(fstream& out, const vector<double>& data);
void readTrainData(const char* outFileName);
void readTestData(const char* outFileName);
map<string, int> PdDistricts;
map<string, int> Categories;
map<string, int> WeekDays;
void Init();

int main() {
	Init();
	readTrainData("data/train_data.txt");
	readTestData("data/test_data.txt");
	return 0;
}


void Init() {
	vector<string> cats = splite(CATEGORIES_String);
	printf("hahah, size=%d\n", int(cats.size()));
	for (int i = 0; i < cats.size(); ++i)
		Categories[cats[i]] = i;

	for (int i = 0; i < 7; ++i)
		WeekDays[DaysInAWeek[i]] = i;
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


int str2int(const string& s) {
	stringstream ss(s);
	int num;
	ss >> num;
	return num;
}


inline double str2double(const string& s) {
	stringstream ss(s);
	double num;
	ss >> num;
	return num;
}


/*
Original string format like: 2015-05-13 01:02:05
Output: {2015, 3, 13, 3725}, where 3725 = 3600*1 + 60*2 + 5

See index:
0123456789012345678
2015-05-13 01:02:05
*/
vector<int> time_to_int(const string& s) {
	vector<int> ans(4);
	ans[0] = str2int(s.substr(0, 4));
	ans[1] = str2int(s.substr(5, 2));
	ans[2] = str2int(s.substr(8, 2));
	int hour = str2int(s.substr(11, 2));
	int minute = str2int(s.substr(14, 2));
	/*int second = str2int(s.substr(17, 2));
	ans[3] = 3600 * hour + 60 * minute + second;*/

	// maybe the seconds is not rather important
	if (minute >= 30)
		++hour;
	ans[3] = hour;

	return ans;
}


int getPdDistrictId(const string& s) {
	if (PdDistricts.find(s) == PdDistricts.end())
		PdDistricts[s] = PdDistricts.size();
	return PdDistricts[s];
}


void output(fstream& out, const vector<double>& data) {
	out << int(data[0]);
	int len = data.size();
	for (int i = 1; i < len; ++i) {
		if (len-i <= 2)
			out << ',' << data[i];
		else
			out << ',' << int(data[i]);
	}
	out << '\n';
}


/*
Total attributes: Dates,Category,Descript,DayOfWeek,PdDistrict,Resolution,Address,X,Y
We use: {
	Dates(to be four attributes: year, month, day, timestamp(the second in a day))
	DayOfWeek(int, 0-6, corresponding to Monday, Tuesday, ..., Sunday),
	PdDistrict(int, I give each PdDistrict an id to identify it),
	Address(No use now, because we have the Longitude and the Latitude),
	X(double, Longitude),
	Y(double, Latitude)

	Resolution(No use now),
	Descript(No use now),
	Category(the label!!!)
}
*/
void readTrainData(const char* outFileName) {
	fstream data("data/train.csv", ios::in);
	fstream out(outFileName, ios::out);
	string line;
	getline(data, line);	// ignore the header line
	out << TrainDataSize << endl;
	out << Row_size << endl;

	while (getline(data, line)) {
		vector<string> vs = splite(line);
		vector<double> data;
		data.push_back(Categories[vs[1]]);			// 1 is the category

		vector<int> time = time_to_int(vs[0]);		// 0 is date
		for (int i = 0; i < time.size(); ++i)
			data.push_back(time[i]);
													// 2 is the Description, skip it
		data.push_back(WeekDays[vs[3]]);			// 3 is DayOfWeek
		data.push_back(getPdDistrictId(vs[4]));		// 4 is PdDistrict
													// 5 is the Resolution, skip it
													// 6 is the Address, skip it
		data.push_back(str2double(vs[7]));			// 7 is X, Longitude
		data.push_back(str2double(vs[8]));			// 8 is Y, Latitude
		output(out, data);
	}

	out.close();
	data.close();
}

/*
Total attributes: Id,Dates,DayOfWeek,PdDistrict,Address,X,Y
We use: {
	Id(int),
	Dates(to be four attributes: year, month, day, timestamp(the second in a day))
	DayOfWeek(int, 1-7, corresponding to Monday, Tuesday, ..., Sunday),
	PdDistrict(int, I give each PdDistrict an id to identify it),
	Address(No use now, because we have the Longitude and the Latitude),
	X(double, Longitude),
	Y(double, Latitude)
}
*/
void readTestData(const char* outFileName) {
	fstream data("data/test.csv", ios::in);
	fstream out(outFileName, ios::out);
	string line;
	getline(data, line);	// ignore the header line
	out << TestDataSize << endl;
	out << Row_size << endl;

	while (getline(data, line)) {
		vector<string> vs = splite(line);
		vector<double> data;
		data.push_back(str2int(vs[0]));				// 0 is the id

		vector<int> time = time_to_int(vs[1]);		// 1 is date
		for (int i = 0; i < time.size(); ++i)
			data.push_back(time[i]);
		data.push_back(WeekDays[vs[2]]);			// 2 is DayOfWeek
		data.push_back(getPdDistrictId(vs[3]));		// 3 is PdDistrict
													// 4 is the Address, skip it
		data.push_back(str2double(vs[5]));			// 5 is X, Longitude
		data.push_back(str2double(vs[6]));			// 6 is Y, Latitude
		output(out, data);
	}

	out.close();
	data.close();
}