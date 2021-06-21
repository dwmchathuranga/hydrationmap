import nmrglue
import pylab
import matplotlib
from scipy.ndimage import gaussian_filter
import numpy as np
dic1, data1 = nmrglue.fileio.bruker.read_pdata(dir="C:\\Bruker\\TopSpin4.0.6\\data\\sydowii_0M\\sydowii_0M_DARR_100ms\\1\\pdata\\1",
                                               bin_files=None, procs_files=None, read_procs=True, acqus_files=None,
                                               read_acqus=True, scale_data=True, shape=None, submatrix_shape=None,
                                               all_components=False, big=None, isfloat=None)
dic2, data2 = nmrglue.fileio.bruker.read_pdata(dir="C:\\Bruker\\TopSpin4.0.6\\examdata\\test1\\116\\pdata\\1",
                                               bin_files=None, procs_files=None, read_procs=True, acqus_files=None,
                                               read_acqus=True, scale_data=True, shape=None, submatrix_shape=None,
                                               all_components=False, big=None, isfloat=None)


# cl = [4000000*1.2**x for x in range(20)] # fungi
# cl2 = [4900000*1.2**x for x in range(5)] # fungi
cl = [55500.0 * 1.2 ** x for x in range(20)]
cl2 = [10004050000.0 * 2.4 ** x for x in range(10)]

# data3 = (data1 * 2 - data2)
#
# data3 = data3/np.max(data3)
# data4 = data3
# data1 = data1


# data3 = data3[385:807, 1027:1134]
# data1 = data1[385:807, 1027:1134]


cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0, "#ff9999"), (0.009, "#ffb3b3"), (0.02, "#ffcccc"),
                                                                (0.07, "#ffffb3"), (0.12, "#ffff80"),
                                                                (0.22, "#ccffcc"),
                                                                (0.305, "#80ffaa"), (0.335, "#4dff88"), (0.415, "#99c2ff"),
                                                                (1, "blue")])


# data3 = gaussian_filter(data3, sigma=5.25)   # noise cancellation
# # data1 = gaussian_filter(data1, sigma=5)   # noise cancellation

# cnt = pylab.contourf(data4, cl, alpha=1, cmap=cmap)
#
# for c in cnt.collections:
#     c.set_edgecolor("face")
#     c.set_linewidth(0.000000001)
#
# pylab.colorbar(cmap="RdYlGn")
cnt = pylab.contour(data1, cl2, alpha=0.4, colors="black")

pylab.savefig("plot_2D_Alex.svg")
pylab.show()
