#include <vector>
#include <unordered_map>
#include <iostream>

int main(void) {
	std::unordered_map<int, std::string> table(
			{
			{4,"X"},
			{5,"Z"},
			{57,"G"},
			{71,"A"},
			{87,"S"},
			{97,"P"},
			{99,"V"},
			{101,"T"},
			{103,"C"},
			{113,"I"},
			{113,"L"},
			{114,"N"},
			{115,"D"},
			{128,"K"},
			{128,"Q"},
			{129,"E"},
			{131,"M"},
			{137,"H"},
			{147,"F"},
			{156,"R"},
			{163,"Y"},
			{186,"W"}
			}
	);
	int count = 0;
	int c = 0;
	while (std::cin >> c) {
		if (c == 0) {
			++count;
		} else {
			++count;
			std::cout << table[count];
			count = 0;
		}
	}
	std::cout << std::endl;
}
