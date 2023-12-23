#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from nxcsv import read_nx_datafile, PlotData


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: plot <filename> [outputfile]")
        print("Where\n filename contains csv data exported from NX\n outputfile is an optional output PDF filename")
        exit()

    vel_filename = sys.argv[1]
    if not os.path.exists(vel_filename):
        print(f"File '{vel_filename}' does not exist")
        exit()

    accel_filename = sys.argv[2]
    if not os.path.exists(accel_filename):
        print(f"File '{accel_filename}' does not exist")
        exit()

    output_filename = None
    if len(sys.argv) == 4:
        output_filename = sys.argv[3]

    print(f"opening {vel_filename}")
    vel_plot_data = read_nx_datafile(vel_filename)
    print(vel_plot_data)

    print(f"opening {accel_filename}")
    accel_plot_data = read_nx_datafile(accel_filename)
    print(accel_plot_data)

    max_accel_index = np.argmax(accel_plot_data.data[:,1])
    min_accel_index = np.argmin(accel_plot_data.data[:,1])

    fig, ax1 = plt.subplots()
    ax1.plot(vel_plot_data.data[:,0], vel_plot_data.data[:,1], label='Angular velocity', color='blue')
    ax1.set_xlabel(vel_plot_data.xlabel)
    ax1.set_ylabel(vel_plot_data.ylabel, color='blue')
    ax1.tick_params('y', colors='blue')
    # ax1.legend(loc="lower left")
    # plt.legend()

    ax2 = ax1.twinx()
    ax2.plot(accel_plot_data.data[:,0], accel_plot_data.data[:,1], label='Angular acceleration', color='red')
    ax2.set_ylabel(accel_plot_data.ylabel, color='red')
    ax2.tick_params('y', colors='red')
    # ax2.legend(loc="upper left")
    # plt.legend()

    plt.axvline(x=vel_plot_data.data[min_accel_index,0], color='gray', linestyle=':', label='Min accel')
    # plt.legend()


    plt.axvline(x=vel_plot_data.data[max_accel_index,0], color='gray', linestyle='--', label='Max accel')
    # plt.legend()


    # plt.xlabel(plot_data.xlabel)
    # plt.ylabel(plot_data.ylabel)
    # plt.plot(plot_data.data[:,0], plot_data.data[:,1])
    # plt.axhline(y=min, color='gray', linestyle='--', label='min')
    # plt.axhline(y=max, color='gray', linestyle='--', label='max')

    # ticks_no_extremas = list(plt.yticks()[0])[2:-2]

    # plt.yticks(ticks_no_extremas + [max] + [min])

    if output_filename is not None:
        plt.savefig(output_filename, format='pdf', bbox_inches='tight')
    else:
        plt.show()

if __name__ == '__main__':
    main()