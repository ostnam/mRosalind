#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(void) {
	int n;
	cin >> n;
	vector<int> heap;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		heap.push_back(x);
	}
	bool sorted = false;
	while (!sorted) {
		sorted = true;
		for (int i = 2; i<=n; i++) {
			if (heap[i-1] > heap[floor(i/2)-1]) {
				swap(heap[i-1], heap[(i/2)-1]);
				sorted = false;
			}
		}
	}
	for (int i = 0; i < n;  i++) {
		cout << heap[i] << " ";
	}
	cout << endl;
}
