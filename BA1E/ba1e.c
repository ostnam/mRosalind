/*				Introduction
 * Given a string Pattern, find every substring of length k which
 * appears at least t times in any substring of Pattern of length L.
 *
 *				Method
 * 1. Read the inputs from stdin (I recommend `cat rosalind_ba1e.c | ./eba1e`)
 * 2. Every correct substring will be stored in a hashmap -> implement a hash map
 * 3. For every substring of correct length, we will 
 *   -> build a count hashmap
 *   -> obtain each kmer, check if it is in the answer hashmap
 * 	-> if it doesn't appear, we will update the value of the count hashmap
 * 	-> if it does, we'll skip this kmer
 * 4. Print every kmer in the result hashmap
 *
 * 				Results
 * 1. The algorithm provides the correct solutions.
 * 2. It takes a few seconds to run, which opens the door to optimizations :
 * 	-> using get_hash more often, right now we call get_bucket multiple
 * 	   times in a row (although I don't expect the hash function to have a
 * 	   big performance impact)
 *	
 *	-> a simpler hash function would also probably work
 * 	-> optimizing the hash table parameters (such as # of bins)
 * 3. I cannot guarantee that memory management is optimal and no memory is left
 *    unreleased *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

unsigned long hash(char *str) {
    unsigned long hash = 5381;
    int c;
    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
} // hash function courtesy of http://www.cse.yorku.ca/~oz/hash.html

typedef struct Entry {
	unsigned count;
	struct Entry *next;
	char *content;
} Entry;

typedef struct {
	unsigned bucket_count;
	Entry **buckets;
} Hashmap;

Hashmap * Hashmap_new(unsigned bucket_count) {
	Hashmap *new = malloc(sizeof(Hashmap));
	if (new == NULL) {
		fprintf(stderr, "error while allocating new Hashmap");
		abort();
	}

	new->buckets = malloc(bucket_count * sizeof(Entry *));
	if (new->buckets == NULL) {
		fprintf(stderr, "error while allocating the buckets of a new Hashmap");
		abort();
	}
	for (int i=0; i < bucket_count; i++) {
		new->buckets[i] = NULL;
	}

	new->bucket_count = bucket_count;
	return new;
}

Entry * Entry_new(char* string) {
	Entry *new = malloc(sizeof(Entry));
	if (new == NULL) {
		fprintf(stderr, "error while allocating new Entry");
		abort();
	}
	new->content = string;
	new->next    = NULL;
	new->count   = 1;
	return new;
}

Entry * get_bucket(Hashmap *target, char *value) {
	unsigned value_hash = hash(value) % (target->bucket_count); // add +1?
	return target->buckets[value_hash];
}

unsigned get_hash(Hashmap *target, char* value) {
	unsigned value_hash = hash(value) % (target->bucket_count); // add +1?
	return value_hash;
}

bool Hashmap_includes(Hashmap *target, char *value) {
	Entry *current_entry = get_bucket(target, value);
	while (current_entry != NULL) {
		if (strcmp(current_entry->content, value) == 0) {
			return true;
		} else {
			current_entry = current_entry->next;
		}
	}
	return false;
}

void Hashmap_set(Hashmap *target, char *value) {
	if (! Hashmap_includes(target, value)) {
		Entry *current_entry = get_bucket(target, value);
		if (current_entry == NULL) {
			target->buckets[get_hash(target, value)] = Entry_new(value);
		} else { 
			while (current_entry->next != NULL) {
				current_entry = current_entry->next;
			}
		current_entry->next = Entry_new(value);
		}
	}
}

int Hashmap_increment(Hashmap *target, char *value) {
	if (Hashmap_includes(target, value)) {
		Entry *current_entry = get_bucket(target, value);
		while (strcmp(current_entry->content, value) != 0) {
			current_entry = current_entry->next;
		}
		return ++current_entry->count;
	} else {
		Hashmap_set(target, value);
		return 1;
	}
}
void Entry_free(Entry* target) {
	if (target != NULL) {
		free(target);
		if (target->content != NULL) {
			free(target->content);
		}
	}
}

void Hashmap_free(Hashmap *target) {
	for (int i=0; i < target->bucket_count; i++) {
		Entry *current = target->buckets[i];
		while (current != NULL) {
			Entry *next = current->next;
			Entry_free(current);
			current = next;
		}
	}
	free(target);
}

char * get_kmer(char* string, int position, int length) {
	char *result = malloc((length * sizeof(char)) + 1);
	int res_position = 0;
	for (int i = 0; i < length; i++) {
		result[i] = string[position+i];
	}
	result[length] = '\0';
	return result;
}

void print_every_entry(Hashmap *target) {
	for (int i=0; i < target->bucket_count; i++) {
		Entry *current = target->buckets[i];
		while (current != NULL) {
			printf("%s ", current->content);
			current = current->next;
		}
	}
	printf("\n");
}

int main(void) {
	size_t p_len = 128;
	size_t p_pos = 0;
	char *pattern = malloc(p_len * sizeof(char));
	char new_char = getc(stdin);
	while (new_char != '\n') {
		pattern[p_pos] = new_char;
		if (++p_pos == p_len) {
			p_len *= 2;
			pattern = realloc(pattern, p_len * sizeof(char));
		}
		new_char = getc(stdin);
	}
	pattern[p_pos] = '\0';
	p_len = p_pos + 1;
	pattern = realloc(pattern, p_len * sizeof(char));

	int k, l, t;
	scanf("%d %d %d", &k, &l, &t);
	Hashmap *result = Hashmap_new(32);
	
	for (int i = 0; i <= p_len - l; i++) {
		Hashmap *count = Hashmap_new(128);
		for (int j = 0; j <= l - k; j++) {
			char *current_kmer = get_kmer(pattern, i+j, k);
			if (! Hashmap_includes(result, current_kmer)) {
				int times_seen = Hashmap_increment(count, current_kmer); 
				if (times_seen == t) {
					Hashmap_increment(result, current_kmer);
				} else if (times_seen != 1) {
					free(current_kmer);
				}
			}
		}
		Hashmap_free(count);
	}
	print_every_entry(result);
	return 0;
}
