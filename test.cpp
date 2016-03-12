#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

#define ll long long
#define INF 0x3f3f3f
#define MAX 100100
const int Mod = 1e9+7;

ll num[MAX];

int main()
{
	int i, j, k, n;
	ll key = 1;
	scanf("%d", &n);
	num[1] = 1;
	num[2] = 2;
	num[3] = 5;
	for(i = 4; i <= n; ++i) {
		key = (key * 3) % Mod;
		num[i] = (num[i-1]*2 + key) % Mod;
	}
	// printf("%I64d\n", num[n]);
	printf("%lld\n", num[n]);

	return 0;
}