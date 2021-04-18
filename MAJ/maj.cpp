#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

int main(void) {
	int k, n;
	cin >> k >> n;
	vector<vector<int>> arrays;
	for (int i = 0; i < k; i++) { // parse vecs
		vector<int> curr;
		arrays.push_back(curr);
		for (int j = 0; j < n; j++) {
			int x;
			cin >> x;
			arrays[i].push_back(x);
		}
	}

	for (int i = 0; i < k; i++) {
		bool printed = false;
		unordered_map<int, int> count {0};
		for (auto x: arrays[i]) {
			int a = ++count[x];
			if (a > arrays[i].size() / 2 ) {
				cout << x << " ";
				printed = true;
				break;
			}
		}
		if (!printed) {
			cout << "-1 ";
		}
	}
	cout << endl;
}

