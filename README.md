# Sequence-Pairwise-Alignment

# Pairwise Sequence Alignment (DNA)

This project implements a simple pairwise sequence alignment tool for comparing two DNA sequences of equal length. It computes match/mismatch scores and visualizes the similarity as a line plot using NumPy and Matplotlib.

---

## Features

- Reads two DNA sequences from a FASTA file using Biopython
- Performs basic position-by-position comparison (match = 1, mismatch = 0)
- Visualizes the alignment results as a binary plot

---

## Example test Case

Compare the beta-globin gene from human and chimpanzee to identify mutations or similarities between the two sequences.

---

## Project Structure
```plaintext
pairwise_alignment_project/
├── Data/
│   ├── sequences.fasta             # Input sequences in FASTA format (test case)
│   └── README_sequences.txt        # Information about the sequences test cases
├── src/
│   ├── utils.py                    # Sequence loading
│   ├── alignment.py                # Comparison 
│   └── plot.py                     # Visualization 
├── main.py                         # Project entry
├── requirements.txt                # Required libraries
└── README.md                       # Project overview
