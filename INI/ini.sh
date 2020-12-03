#!/bin/sh
cat rosalind_ini.txt | fold -w 1 | sort | uniq -c | sed 's/[ACGT]//' | tr -d '\n'
