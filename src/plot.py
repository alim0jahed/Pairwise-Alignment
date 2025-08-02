import matplotlib.pyplot as plt

def plot_match(match_arr):
    """
    Plots a line graph showing 1 for match and 0 for
    mismatch for each position
    """

    plt.figure(figsize=(10, 2))
    plt.plot(match_arr, drawstyle="steps-mid", color="blue")
    plt.title("Pairwise alignment Similarity")
    plt.xlabel("Position in Sequence")
    plt.ylabel("Similarity")
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
