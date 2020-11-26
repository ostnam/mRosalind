#!/bin/sh

echo "" > results.txt

while IFS="" read -r p || [ -n "$p" ]
do
  if [ ! -f "$p".fasta ]; then  
  urlP=$(echo "$p" | sed 's/_*//')
  curl -L https://www.uniprot.org/uniprot/"$urlP".fasta --output "$p".fasta
  fi
  if cat "$p".fasta | sed '/^>/d' | tr -d '\n' | grep -q [N][^P][ST][^P]; then
    echo "$p" >> results.txt
    echo $(cat "$p".fasta | sed '/^>/d' | tr -d '\n' | sed '1s/^/ /' | python3 matchpattern.py) >> results.txt
  fi
done < rosalind_mprt.txt

sed -i '/^[[:space:]]*$/d' results.txt 
cat results.txt

exit
