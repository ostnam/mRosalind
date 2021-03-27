#include <stdio.h>
#include <stdlib.h>


void populate(int *array, int len, FILE *fp) {
	for (int i = 0; i < len; i++) {
		fscanf(fp, "%d", &array[i]);
	}
}

int bins(int *arr, int arr_len, int value) {
	int start = 0;
	int end = arr_len - 1;
	int mid;
	while (start <= end) {
		mid = (start + end) / 2;
		if (arr[mid] == value) {
			return mid + 1;
		} else if (arr[mid] > value) {
			end = mid - 1;
		} else {
			start = mid + 1;
		}
	}
	return -1;
}

int main(void) {
	FILE *fp = fopen("rosalind_bins.txt", "r");
	int n, m;
	fscanf(fp, "%d %d", &n, &m);

	int *A = malloc(n * sizeof(int));
	populate(A, n, fp);

	int *list = malloc(m * sizeof(int));
	populate(list, m, fp);

	for (int i = 0; i < m; i++) {
		printf("%d ", bins(A, n, list[i]));
	}
	printf("\n");
}
