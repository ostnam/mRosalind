#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	char *text = malloc(1000*sizeof(char));
	scanf("%s", text);
	size_t len = strlen(text);

	int k;
	scanf("%d", &k);

	long double *(*profile) = malloc(k*sizeof(long double*));
	for (int i = 0; i < k; i++) {
		profile[i] = malloc(4*sizeof(long double));
	}

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < k; j++) {
			scanf("%Le", &profile[i][j]);
		}
		getchar();
	}

	char profile_most[k];
	long double profile_most_prob = 0.0;

	for (int i = 0; i <= len - k; i++) {
		long double result = 1.0;
		for (size_t j = 0; j < k; j++) {
			if (text[i+j] == 'A') {
				result *= profile[0][j];
			} else if (text[i+j] == 'C') {
				result *= profile[1][j];
			} else if (text[i+j] == 'G') {
				result *= profile[2][j];
			} else if (text[i+j] == 'T') {
				result *= profile[3][j];
			}
		}
		if (result > profile_most_prob) {
			for (size_t j = 0; j < k; j++) {
				profile_most[j] = text[i+j];
			}
			profile_most_prob = result;
		}
	}

	for (int i = 0; i < k; i++) {
		printf("%c", profile_most[i]);
	}
	printf("\n");
}
