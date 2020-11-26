#!/bin/sh

echo "" > results.txt

while IFS="" read -r p || [ -n "$p" ]
do
  if [ ! -f "$p".fasta ]; then  
  urlP=$(echo "$p" | sed 's/_*//')
  echo "$urlP"
  curl -L https://www.uniprot.org/uniprot/"$urlP".fasta --output "$p".fasta
  fi
  echo "$p" >> results.txt
  echo $(cat "$p".fasta | sed '/^>/d' | tr -d '\n' | sed '1s/^/ /' | python3 matchpattern.py) >> results.txt
done < rosalind_mprt.txt

cat results.txt

exit
