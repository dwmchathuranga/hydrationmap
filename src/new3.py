import nmrglue
import pylab
import matplotlib
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import numpy as np
import copy
x = 165000  # remove noise level, change 200000

# standard color scale
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0, "#ff0000"), (0.005, "#ff3333"), (0.009, "#ff4d4d"),
                                                                (0.045, "#ffff80"), (0.090, "#ffff66"), (0.15, "#ffff4d"),
                                                                (0.20, "#ffff33"), (0.28, "#99e699"), (0.35, "#85e085"),
                                                                (0.4, "#00cc44"), (0.55, "#00b33c"),
                                                                (0.65, "#8080ff"), (0.82, "#6666ff"),
                                                                (0.96, "#3333ff"), (1, "#0000ff")])
#
# cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0, "#ff0000"), (0.005, "#ff3333"), (0.009, "#ff4d4d"),
#                                                                 (0.035, "#ffff80"), (0.150, "#ffff66"), (0.2, "#ffff4d"),
#                                                                 (0.25, "#ffff33"), (0.38, "#99e699"), (0.52, "#85e085"),
#                                                                 (0.6, "#00cc44"), (0.65, "#00b33c"),
#                                                                 (0.7, "#8080ff"), (0.85, "#6666ff"),
#                                                                 (0.96, "#3333ff"), (1, "#0000ff")])
#
# cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [
#                                                                 (0, "#ff0000"), (0.25, "#ffff4d"),
#                                                                  (0.5, "#66ff66"),
#                                                                 (0.75, "#3333ff"), (1, "#0000ff")])

# get bruker data( create file "test", add all control and water-edited spectra)
def get_data():
    k = []
    j = 0
    t = []
    for i in ["1000", "1001", "1002", "1003", "1004", "1005","1006","1007"]:
        dic, data = nmrglue.fileio.bruker.read_pdata(dir="C:\\Bruker\\TopSpin4.0.6\\examdata\\test\\" + i +"\\pdata\\1",
                                                   bin_files=None, procs_files=None, read_procs=True, acqus_files=None,
                                                   read_acqus=True, scale_data=True, shape=None, submatrix_shape=None,
                                                   all_components=False, big=None, isfloat=None)
        if j % 2 == 0:
            t = []
            t.append(data)
        else:
            t.append(data)
            k.append(copy.deepcopy(t))
        j = j + 1
    return k

# remove noise level, change 200000 as you wish
def set_data(lists):
    lists2 = []
    l = 0
    t = []
    for i in lists:
        for j in i:
            j = np.asarray(j)
            j[j < x] = 0
            if l % 2 == 0:
                t = []
                t.append(j)
            else:
                t.append(j)
                lists2.append(copy.deepcopy(t))
            l = l + 1
    return lists2

# S/S0 ratio
def cal(S1_contl, S1_wtr):
    for key1, value1 in enumerate(S1_contl):
        for key2, val in enumerate(value1):
            try:
                if S1_contl[key1, key2] > 0:
                    data3[key1, key2] = (S1_wtr[key1, key2] * 0.5/ S1_contl[key1, key2])
                else:
                    data3[key1, key2] = 0
            except:
                data3[key1, key2] = 0
    return data3

graph_data = []

for S1_contl, S1_wtr in set_data(get_data()):
    plot = []
    data3 = np.copy(S1_wtr)
    data4 = cal(S1_contl, S1_wtr)

    # select area
    data5 = data4[2:431, 719:842] # for hydration map
    data6 = data4[381:817, 1028:1136]
    # data1 = data1[3:436, 708:866] # for contour lines
    print(np.max(data5))

    # data4 = data4/np.max(data4)


    for key1, value1 in enumerate(data4):
        for key2, val in enumerate(value1):
            if data4[key1, key2] > 1:
                data4[key1, key2] = 0.9936

    print(np.max(data5))

    # create contour
    cl = [0.0125 * 1.2 ** x for x in range(25)] # for hydration map
    cl2 = [0.01 * 2.4 ** x for x in range(10)] # for contour lines

    # noise cancellation
    data6 = gaussian_filter(data6, sigma=0.56) # for hydration map
    # data1 = gaussian_filter(data1, sigma=0.8) # for contour lines
    plot.append(copy.deepcopy(data5)) # for lignin region (only for plants)
    plot.append(copy.deepcopy(data6)) # for polysaccharide region
    graph_data.append(copy.deepcopy(plot))

fig, axs = plt.subplots(nrows=len(graph_data), ncols=2, figsize=(4, 4), constrained_layout=True) # change ncols if you plot two regions

for i in range(len(graph_data)):
    for j in range(2):
        plt.axes(axs[i][j])
        clt = pylab.contourf(graph_data[i][j], cl, alpha=1,cmap=cmap) # for hydration map
        for c in clt.collections:
            c.set_edgecolor("face")
            c.set_linewidth(0.000000001)


pylab.colorbar(cmap="cmap")
# cnt = pylab.contour(data1, cl2, alpha=0.1, colors="black") # for contour lines

pylab.savefig("Hydration_plot.svg")
pylab.show()
