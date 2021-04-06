#include <stdio.h>
#include <stdlib.h>

int main(void) {
	unsigned pattern_length = 32;
	int pattern_position = 0;
	char *pattern = malloc(pattern_length * sizeof(char));
	char c = getc(stdin);
	while (c != '\n') {
		pattern[pattern_position] = c;
		++pattern_position;
		c = getc(stdin);
		if (pattern_position == pattern_length) {
			pattern_length *= 2;
			pattern = realloc(pattern, pattern_length * sizeof(char));
		}
	}
	pattern[pattern_position] = '\0';
	pattern_length = pattern_position++;

	unsigned seq_length = 1024;
	int seq_position = 0;
	char *seq = malloc(seq_length * sizeof(char));
	c = getc(stdin);
	while (c != '\n') {
		seq[seq_position] = c;
		++seq_position;
		c = getc(stdin);
		if (seq_position == seq_length) {
			seq_length *= 2;
			seq = realloc(seq, seq_length * sizeof(char));
		}
	}
	seq[seq_position] = '\0';
	seq_length = seq_position++;
	
	for (unsigned i = 0; i <= seq_length - pattern_length; ++i) {
		int match = 1;
		for (unsigned j = 0; j < pattern_length; ++j) {
			if (seq[i+j] != pattern[j]) {
				match = 0;
				break;
			}
		}
		if (match == 1) {
			printf("%d ", i);
		}
	}
	printf("\n");
	return 0;
}
