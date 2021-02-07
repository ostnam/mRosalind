#include <stdio.h>
#include <stdlib.h>

int main() {
	unsigned n, m, l; // length of each array
	int *A, *B; // 2 given sorted arrays

	scanf("%d", &n); // get n from stdin
	A = malloc(n * sizeof(*A)); // allocate memory for A
	for (int i=0; i<n; i++) {
		scanf("%d", &A[i]);
	} // reads each int from stdin to A

	scanf("%d", &m);
	B = malloc(m * sizeof(*B));
	for (int i=0; i<m; i++) {
		scanf("%d", &B[i]);
	} // same block for B

	l = m + n; // length of final array
	int C[l];
	int a_position, b_position = 0;
	for (int i = 0; i<l; i++) {
		if (a_position == n) {
			C[i] = B[b_position];
			b_position +=1;
			continue;
		} else if (b_position == m) {
			C[i] = A[a_position];
			a_position +=1;
			continue;
		}
		if (A[a_position] < B[b_position]) {
			C[i] = A[a_position];
			a_position += 1;
		} else {
			C[i] = B[b_position];
			b_position +=1;
		}
	}

	for (int i = 0; i<l; i++) {
		printf("%d ", C[i]);
	}
	puts("");
	return 0;
}
