#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	int k, n;
	cin >> k >> n;
	for (int i = 0; i < k; i++) { // for each array
		vector<int> current;
		int index = -1;       // result of each line
		for (int j = 0; j < n; j++) {
			int x;
			cin >> x;
			if (find(current.begin(), current.end(), -x) != current.end()) {
				index = distance(current.begin(), find(current.begin(), current.end(), -x));
				cout << index + 1 << " " << j + 1 << endl; // +1 because the problem uses arrays starting at index 1
				cin.ignore(1000000000000, '\n');           // skip to the next line, this is my first c++ program and I don't know if there's a more elegant way to do this
				break;
			} else {
				current.push_back(x);
				}
			}
		if (index == -1) {
			cout << index << endl;
		}
	}
}
