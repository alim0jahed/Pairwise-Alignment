import numpy as np

def pairwise_match_arrays(seq1, seq2):
    """
    Compares two sequences and returns a Numpy array of 1s and 0s.
    1 for matches and 0 for mismatches.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have same length")
    return np.array([1 if a == b else 0 for a, b in zip(seq1, seq2)])