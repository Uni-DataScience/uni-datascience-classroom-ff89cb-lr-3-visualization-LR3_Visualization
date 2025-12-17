import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    """
    Plots a 1D line plot.

    Parameters:
    data (array): A sequence of values to plot.
    """
    plt.figure(figsize=(6, 4))
    plt.plot(data, label='Line Plot')
    plt.title('1D Line Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


def plot_2d(x, y):
    """
    Plots a 2D scatter plot.

    Parameters:
    x (array): x-values.
    y (array): y-values.
    """
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, color='b', label='Data Points')
    plt.title('2D Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


def plot_3d(x, y, z):
    """
    Plots a 3D scatter plot.

    Parameters:
    x (array): x-values.
    y (array): y-values.
    z (array): z-values.
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis')
    ax.set_title('3D Scatter Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)