#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from nxcsv import read_nx_datafile, PlotData


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: plot <filename> [outputfile]")
        print("Where\n filename contains csv data exported from NX\n outputfile is an optional output PDF filename")
        exit()

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

    max = np.max(plot_data.data[:,1])
    min = np.min(plot_data.data[:,1])

    plt.title(plot_data.title)
    plt.xlabel(plot_data.xlabel)
    plt.ylabel(plot_data.ylabel)
    plt.plot(plot_data.data[:,0], plot_data.data[:,1])
    plt.axhline(y=min, color='gray', linestyle='--', label='max')
    plt.axhline(y=max, color='gray', linestyle='--', label='max')

    ticks_no_extremas = list(plt.yticks()[0])[2:-2]

    plt.yticks(ticks_no_extremas + [max] + [min])

    if output_filename is not None:
        plt.savefig(output_filename, format='pdf', bbox_inches='tight')
    else:
        plt.show()

    # numpy.savetxt('test.csv', plot_data.data, delimiter=',') 

if __name__ == '__main__':
    main()