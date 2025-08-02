from src.utils import read_fasta
from src.alignment import pairwise_match_arrays
from src.plot import plot_match

def main():
    fasta_path = 'Data/sequences.fasta'

    seq1, seq2 = read_fasta(fasta_path)
    match_array = pairwise_match_arrays(seq1, seq2)
    plot_match(match_array)

main()