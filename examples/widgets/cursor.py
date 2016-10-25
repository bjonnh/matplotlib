"""
==================
Interactive cursor
==================

Adds an interactive cursor to the plot. This cursor is for display
purpose only.
"""

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.widgets import Cursor


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#FFFFCC')

x, y = 4*(np.random.rand(2, 100) - .5)
ax.plot(x, y, 'o')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# set useblit = True on gtkagg for enhanced performance
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

plt.show()
