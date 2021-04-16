#include <vector>
#include <unordered_map>
#include <iostream>

int main(void) {
	std::unordered_map<std::string, int> table(
			{
			{"X", 4},
			{"Z", 5},
			{"G", 57},
			{"A", 71},
			{"S", 87},
			{"P", 97},
			{"V", 99},
			{"T", 101},
			{"C", 103},
			{"I", 113},
			{"L", 113},
			{"N", 114},
			{"D", 115},
			{"K", 128},
			{"Q", 128},
			{"E", 129},
			{"M", 131},
			{"H", 137},
			{"F", 147},
			{"R", 156},
			{"Y", 163},
			{"W", 186}
			}
	);
	std::vector<int> result;
	std::string peptide;
	std::cin >> peptide;
	for (auto &residue: peptide) {
		int x = table[std::string(1, residue)];
		for (int i = 0; i < x - 1; i++) {
			result.push_back(0);
		}
		result.push_back(1);
	}
	for (auto &i: result) {
		std::cout << i << " ";
	}
}
