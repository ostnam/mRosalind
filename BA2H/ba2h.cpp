#include <iostream>
#include <string>
#include <vector>
using namespace std;

int hamming_distance(string& a, string& b) {
	int result = 0;
	for (int i = 0; i < a.size(); i++) {
		if (a[i] != b[i]) {
			result++;
		}
	}
	return result;
}

int DBPAS(string& pattern, vector<string>& dna) {
	int k = pattern.size();
	int distance = 0;
	for (auto text: dna) {
		int hd = 100000;
		for (int i = 0; i <= text.size() - k; i++) {
			string curr_kmer = text.substr(i, k);
			int curr_hd = hamming_distance(pattern, curr_kmer);
			if (curr_hd < hd) {
				hd = curr_hd;
			}
		}
		distance += hd;
	}
	return distance;
}


int main(void) {
	string pattern;
	cin >> pattern;
	string curr;
	vector<string> dna;
	while (cin >> curr) {
		dna.push_back(curr);
	}
	cout << DBPAS(pattern, dna) << endl;
}
