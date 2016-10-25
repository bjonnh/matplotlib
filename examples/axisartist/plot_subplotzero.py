"""
=========================
Create zero-centered axes
=========================

This example demonstrates how to use SubplotZero to create
zero-centered axes.
"""

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.axisartist.axislines import SubplotZero

if 1:
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    # Display the zero-centered axes

    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_visible(True)

    # Disable the box axes

    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)

    x = np.linspace(-0.5, 1., 100)
    ax.plot(x, np.sin(x*np.pi))

    plt.show()
