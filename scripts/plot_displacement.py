#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from nxcsv import read_nx_datafile, PlotData

def main():
    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist")
        exit()

    output_filename = None
    if len(sys.argv) == 3:
        output_filename = sys.argv[2]

    print(f"opening {filename}")
    plot_data = read_nx_datafile(filename)
    print(plot_data)

    max_angle = np.min(plot_data.data[:,1])

    plt.title(plot_data.title)
    plt.xlabel(plot_data.xlabel)
    plt.ylabel(plot_data.ylabel)
    plt.plot(plot_data.data[:,0], plot_data.data[:,1])
    plt.ylim(-100, 0)
    plt.axhline(y=max_angle, color='gray', linestyle='--', label='Max Angle')
    plt.yticks(list(plt.yticks()[0]) + [max_angle])

    if output_filename is not None:
        plt.savefig(output_filename, format='pdf', bbox_inches='tight')

    # plt.show()

    # numpy.savetxt('test.csv', plot_data.data, delimiter=',') 

if __name__ == '__main__':
    main()
