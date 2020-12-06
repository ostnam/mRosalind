# cat a file contaning the protein ids and pipe it to this script
# ie cat test | python3 dbpr.py
from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO

import sys
prots_list = []
for line in sys.stdin:
    clean_line = line.strip()
    prots_list.append(clean_line)

for id in prots_list:
    with ExPASy.get_sprot_raw(id) as name:
        prot_record = SeqIO.read(name, "swiss")
        result = prot_record.annotations["keywords"]
        print(id)
        [print(i) for i in result]
        print("")
