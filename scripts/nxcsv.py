import numpy
from typing import Optional

class PlotData:
    def __init__(self, title: str):
        self.title: str = title
        self.xlabel: str = ""
        self.ylabel: str = ""
        self.data:Optional[numpy.ndarray]  = None

    def __repr__(self):
        return f"Title: {self.title}\nX label: {self.xlabel}\nY label: {self.ylabel}"

def read_nx_datafile(filename:str) -> PlotData:
    # the files contain '\ufeff' (Byte Order Mark) that can be ignored
    # use utf-8-sig instead of plain utf-8 to get rid of the BOM mark in our data
    with open(filename, 'r', encoding='utf-8-sig') as fd:
        data = fd.read()

    lines = data.split('\n\n')
    # remove the leading #
    plot_data = PlotData(lines[0][1:])

    # also remove the leading #
    (plot_data.xlabel, plot_data.ylabel) = lines[1][1:].split(',')

    data_list = [[float(x) for x in line.split(',')] for line in lines[2:] if ',' in line]

    plot_data.data = numpy.array(data_list)
    return plot_data
