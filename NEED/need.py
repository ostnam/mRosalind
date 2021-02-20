from sys import argv
from Bio import Entrez

Entrez.email = "enter_your@email_adress.com"

def download_fasta_from_entrez(seq_id):
    with open(seq_id, 'w') as f:
        handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
        record = handle.read()
        f.write(record.rstrip('\n'))


if __name__ == "__main__":
    for i in argv[1:]:
        print(f"Now trying to download {i}...")
        try:
            download_fasta_from_entrez(i)
        except:
            print(f"The script had an error trying to download {i}")
        else:
            print(f"Successfully downloaded {i}")
