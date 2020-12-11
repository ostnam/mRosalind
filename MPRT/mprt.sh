#!/bin/bash
# My solution to the Rosalind MPRT problem

echo "" > results.txt

while IFS="" read -r p || [ -n "$p" ]
do
  if [ ! -f "$p".fasta ]; then  
  urlP=$(echo "$p" | sed 's/_*//')
  curl -L https://www.uniprot.org/uniprot/"$urlP".fasta --output "$p".fasta # downloads the missing files from uniprot if they don't exist in the directory
  fi
  if cat "$p".fasta | sed '/^>/d' | tr -d '\n' | grep -q -m 1 [N][^P][ST][^P]; then # finds if there's at least one match with grep, commands before grep clean the FASTA file of the metadata about the sequence
    echo "$p" >> results.txt
    echo $(cat "$p".fasta | sed '/^>/d' | tr -d '\n' | sed '1s/^/ /' | python3 matchpattern.py) >> results.txt # uses the matchpattern python script because grep doesn't find overlapping matches (ie NNTSM, where the second character of the first match is the first of the second match)
  fi
done < rosalind_mprt.txt

sed -i '/^[[:space:]]*$/d' results.txt 
cat results.txt

exit
