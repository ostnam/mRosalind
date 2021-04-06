#include <stdio.h>
#include <stdlib.h>

char rc(char base) {
	switch (base) {
		case 'A':
			return 'T';
		case 'T':
			return 'A';
		case 'G':
			return 'C';
		case 'C':
			return 'G';
		default:
			abort();
	}
}

int main(void) {
	char c;
	unsigned dna_len = 128;
	int dna_pos = 0;
	char *dna = malloc(dna_len * sizeof(char));
	while (1) {
		if (dna_pos == dna_len) {
			dna_len *= 2;
			dna = realloc(dna, dna_len*sizeof(char));
		}
		c = getc(stdin);
		if (c != 'A' &&
		    c != 'C' &&
		    c != 'G' &&
		    c != 'T') {
			break;
		}
		dna[dna_pos] = c;
		++dna_pos;
	}
	dna[dna_pos] = '\0';
	dna = realloc(dna, (dna_pos+1) * sizeof(char));
	--dna_pos;
	for (; dna_pos >= 0; --dna_pos) {
		char r = rc(dna[dna_pos]);
		printf("%c", r);
	}
	printf("\n");
	return 0;
}
