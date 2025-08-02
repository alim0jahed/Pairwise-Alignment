from Bio import SeqIO

def read_fasta(file_path):
    """
    Reads a Fasta file and returns the sequence as strings

    """

    records = list(SeqIO.parse(file_path, "fasta"))
    if len(records) != 2:
        raise ValueError("Fasta file must contain exactly two sequences")

    seq1 = str(records[0].seq).upper()
    seq2 = str(records[1].seq).upper()

    return seq1, seq2