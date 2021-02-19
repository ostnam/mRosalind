#!/bin/bash
n=$(head -n1 "$1")
len=$(wc -l < "$1")  # < operator avoids wc from printing filename
result=$((n-len))  # len is number of edges + 1 since the first line is counted
echo "$result"
exit
