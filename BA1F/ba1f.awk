#!/bin/awk -f

END {
	minimum       = 0
	current_score = 0
	minimums      = "0"
	for (i = 1; i <= length($0); i++) {
		char = substr($0, i, 1)
		if (char == "C") {
			current_score--
		} else if (char == "G") {
			current_score++
		}

		if (current_score < minimum) {
			minimums = i
			minimum = current_score
		} else if (current_score == minimum) {
			minimums = minimums " " i
		}
	}
	print minimums
}
