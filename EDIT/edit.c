// my solution to the EDIT problem
// multiline fasta sequences must be merged to a single line per sequence, so that line 2 and 4 are the compared sequences
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	FILE *file = fopen("rosalind_edit.txt", "r");
	
	char *ignored_line = NULL;
	size_t ignored_line_size = 0;

	char *string_a = NULL;
	char *string_b = NULL;
	size_t size_a = 0;
	size_t size_b = 0;

	getline(&ignored_line, &ignored_line_size, file);
	getline(&string_a, &size_a, file);
	getline(&ignored_line, &ignored_line_size, file);
	getline(&string_b, &size_b, file);
	
	int (*comparison_array)[strlen(string_b)];
	comparison_array = malloc((strlen(string_a)+1) * (strlen(string_b)+1) * sizeof(int));

	for (int i = 0; i <= strlen(string_a); i++) {
		for (int j = 0; j <= strlen(string_b); j++) {
			if (i == 0) {
				comparison_array[i][j] = j;
			} else if (j == 0) {
				comparison_array[i][j] = i;
			} else if (string_a[i-1] == string_b[j-1]) {
				comparison_array[i][j] = comparison_array[i-1][j-1];
			} else {
				if (comparison_array[i-1][j-1] < comparison_array[i][j-1]) {
					if (comparison_array[i-1][j-1] < comparison_array[i-1][j]) {
						comparison_array[i][j] = comparison_array[i-1][j-1] + 1;
					} else {
						comparison_array[i][j] = comparison_array[i-1][j] + 1;
					}
				} else {
					if (comparison_array[i][j-1] < comparison_array[i-1][j]) {
						comparison_array[i][j] = comparison_array[i][j-1] + 1;
					} else {
						comparison_array[i][j] = comparison_array[i-1][j] + 1;
					}
				}
			}
		}
	}
	printf("%d\n", comparison_array[strlen(string_a)][strlen(string_b)]);
	return 0;
}
