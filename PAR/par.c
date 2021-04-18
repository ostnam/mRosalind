#include <stdio.h>
#include <stdlib.h>

void shiftup_and_swap(int *arr, int begin, int end) {
	// move every int between begin and end to the next index
	// end value will be moved to begin
	int tmp = arr[end];
	for (int i = end; i > begin; i--) {
		arr[i] = arr[i-1];
	}
	arr[begin] = tmp;
}

int main(void) {
	/* 	Parsing input	 */
	int n;
	scanf("%d", &n);
	int arr[n];
	for (int i = 0; i < n; i++) {
		int *x = &arr[i];
		scanf("%d", x);
	}

	/* moving the first value up until it's < to the next one */
	int curr_pos = 0;
	while (arr[curr_pos] > arr[curr_pos + 1] && curr_pos < n) {
		int tmp = arr[curr_pos + 1];
		arr[curr_pos + 1] = arr[curr_pos];
		arr[curr_pos] = tmp;
		curr_pos++;
	}
	
	/*    moving every value < to the separator before it    */
	for (int i = curr_pos; i < n; i++) {
		if (arr[i] < arr[curr_pos]) {
			shiftup_and_swap(arr, curr_pos, i);
			curr_pos++;
		}
	}

	/* 	Printing result	       */
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}
