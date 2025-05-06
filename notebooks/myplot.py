#
# -*- coding: utf-8 -*-
#

"""
My plot
"""

import numpy as np
import matplotlib.pyplot as plt

class MyPlot:
    """
    """

    fig_size = (10, 10)
    lin_points = 1000
    ticks_frequency = 1

    @staticmethod
    def parabola(a, b, c, x):
        y = a*x**2 + b*x + c
        return y

    @staticmethod
    def cartesian(fct, xmin, xmax, ymin, ymax):
        """
        Adapted from:
        how-i-can-get-cartesian-coordinate-system-in-matplotlib
        https://stackoverflow.com/questions/13430231/
        """

        lin_points = MyPlot.lin_points
        fig_size = MyPlot.fig_size
        ticks_frequency = MyPlot.ticks_frequency

        x = np.linspace(xmin, xmax, lin_points)
        y = fct(x) # x**2 - 4*x - 5

        # Plot points
        fig, ax = plt.subplots(figsize=fig_size)
        ax.plot(x,y)

        # Set identical scales for both axes
        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

        # Set bottom and left spines as x and y axes of coordinate system
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Create 'x' and 'y' labels placed at the end of the axes
        ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
        ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

        # Create custom major ticks to determine position of tick labels
        x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])

        # Create minor ticks placed at each integer to enable drawing of 
        # minor grid
        # lines: note that this has no effect in this example with 
        # ticks_frequency=1
        ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax+1), minor=True)
        
        # Draw major and minor grid lines
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-',
                                                                   alpha=0.2)

        # Draw arrows
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(),
                                                                 **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(),
                                                                 **arrow_fmt)
        # Done:
        plt.show()
