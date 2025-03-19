from Bio import SeqIO
import sys

def fasta_to_tab(input_file, output_file):
    with open(output_file, 'w') as out_f:
        for record in SeqIO.parse(input_file, 'fasta'):
            out_f.write(f"{record.id}\t{str(record.seq)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fasta_to_tab.py <input.fasta> <output.tsv>")
    else:
        fasta_to_tab(sys.argv[1], sys.argv[2])