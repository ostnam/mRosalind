#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main(void) {
	int k, n;
	cin >> k >> n;
	for (int i = 0; i < k; i++) { // for each array
		vector<int> current;
		unordered_set<int> seen;
		int index = -1;       // result of each line
		for (int j = 0; j < n; j++) {
			int x;
			cin >> x;
			for (int h = 0; h < current.size(); h++) {
				int a = x + current[h];	
				if (seen.count(-a) == 1) {
					index = distance(current.begin(), find(current.begin(), current.end(), -a));
					vector<int> result = {index + 1, j + 1, h + 1};
					sort(result.begin(), result.end());
					cout << result[0] << " " << result[1] << " " << result[2] << endl; 
					cin.ignore(1000000000000, '\n');
				break;
				} 
			}
			if (index != -1) {
				break;
			} else {
				current.push_back(x);
				seen.insert(x);
			}
		}
		if (index == -1) {
			cout << index << endl;
		}
	}
}

