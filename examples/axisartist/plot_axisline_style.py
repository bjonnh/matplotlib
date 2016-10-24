"""
========================
Customize the axis style
========================

This example demonstrates how to customize axes style of a Subplot.
"""

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.axisartist.axislines import Subplot

if 1:
    fig = plt.figure(1)
    ax = Subplot(fig, 111)
    fig.add_subplot(ax)

    for direction in ["left", "bottom"]:
        ax.axis[direction].set_axisline_style("-|>")

    x = np.linspace(-0.5, 1., 100)
    ax.plot(x, np.sin(x*np.pi))

    plt.show()
