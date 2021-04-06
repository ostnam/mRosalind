#include <stdio.h>
#include <stdlib.h>

int main(void) {
	unsigned str_len = 64;
	char *string = malloc(str_len * sizeof(char));
	unsigned str_pos = 0;
	char char_read = getc(stdin);
	while (char_read != '\n') {
		if (str_pos == str_len) {
			str_len *= 2;
			if (str_len < str_pos) {
				fprintf(stderr, "str_len overflow, input too long");
				abort();
			}
			string = realloc(string, str_len);
		}
		string[str_pos] = char_read;
		str_pos += 1;
		char_read = getc(stdin);
	}
	string[str_pos] = '\0'; // last char read will be \n, replace it with null char
	str_len = str_pos;
	string = realloc(string, str_pos * sizeof(char));

	unsigned pat_len = str_len;
	char *pat = malloc(pat_len * sizeof(char));
	unsigned char_pos = 0;
	char_read = getc(stdin);
	while (char_read != '\n') {
		pat[char_pos] = char_read;
		char_pos += 1;
		char_read = getc(stdin);
	}
	pat[char_pos] = '\0';
	pat = realloc(pat, char_pos);
	pat_len = char_pos;
	
	unsigned count = 0;
	for (unsigned i = 0; i <= str_len - pat_len; i++) {
		unsigned errors = 0;
		for (unsigned j = 0; j < pat_len; j++) {
			if (string[i+j] != pat[j]) {
				++errors;
			}
		}
		if (errors == 0) {
			++count;
		}
	}

	printf("%d\n", count);
	return 0;
}
