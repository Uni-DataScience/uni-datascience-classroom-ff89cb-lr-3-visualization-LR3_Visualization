import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    counter = collections.Counter(data)

    categories = list(counter.keys())
    frequencies = list(counter.values())

    fig, ax = plt.subplots()
    ax.bar(categories, frequencies, color=['skyblue', 'lightgreen', 'lightcoral'])

    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Categories')

    plt.show()
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)