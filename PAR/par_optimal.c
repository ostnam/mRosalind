// implementation of the optimal solution suggested by cburshka
// in practice around 2x faster than my initial solution (~50 vs ~100ms)
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	/* 	Parsing input	 */
	int n;
	scanf("%d", &n);
	int arr[n];
	for (int i = 0; i < n; i++) {
		int *x = &arr[i];
		scanf("%d", x);
	}

	int a = 0;
	int b = n;
	while (a < b) {
		if (arr[b] > arr[0]) {
			--b;
		} else if ( arr[a] <= arr[0] ) {
			++a;
		} else {
			int tmp = arr[a];
			arr[a] = arr[b];
			arr[b] = tmp;
		}
	}
	int tmp = arr[a];
	arr[a] = arr[0];
	arr[0] = tmp;

	/* 	Printing result	       */
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}
