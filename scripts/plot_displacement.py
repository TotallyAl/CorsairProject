#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt
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

    plt.title(plot_data.title)
    plt.xlabel(plot_data.xlabel)
    plt.ylabel(plot_data.ylabel)
    plt.plot(plot_data.data[:,0], plot_data.data[:,1])
    if output_filename is not None:
        plt.savefig(output_filename, format='pdf', bbox_inches='tight')

    plt.show()

    # numpy.savetxt('test.csv', plot_data.data, delimiter=',') 

if __name__ == '__main__':
    main()