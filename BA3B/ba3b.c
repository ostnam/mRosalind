#include <stdio.h>

int main(void) {
	char last;
	char now;
	while ((now = getchar()) != '\n') {
		putchar(now);
	}
	while (now = getchar()) {
		if (now == EOF) {
			break;
		} else if (now == '\n') {
			putchar(last);
		} else {
			last = now;
		}
	}
	putchar('\n');
}
