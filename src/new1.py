import nmrglue as ng
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
cs_values = [103.43, 74.29, 86.63, 68.23, 77.26, 61.23, 103.5, 55.09, 72.9, 83.23, 75.7, 60.48, 101.0, 71.7, 84.44,
             71.9, 69.85, 60.3]  # chemical shifts values which read from spectrum
data1 = [cs_values[x:x + 6] for x in range(0, len(cs_values), 6)]
contour_start = 30 # contour level start value
contour_num = 10  # number of contour levels
contour_factor = 1.20  # scaling factor between contour levels

cl = contour_start * contour_factor ** np.arange(contour_num)
print(cl)
data = np.array(data1)
print(data)
x0= 1
y0= 1.5
x1= 1.2
y1= 1.7

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contour(data, cl, extent=(0, data.shape[1] - 1, 0, data.shape[0] - 1))
#
# #
# if x0 > x1:
#     x0, x1 = x1, x0
# if y0 > y1:
#     y0, y1 = y1, y0
#
# # plot a box around each peak and label
# ax.plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0], 'k')
# # ax.text(x1 + 1, y0, name, size=textsize, color='r')
#
#
plt.show()