import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import xlrd
import matplotlib.pyplot as plt
loc = ('C:\\Users\\Malitha\\PycharmProjects\\untitled2\\src\\1.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)
x1 = []
y= []
z =[]
d =[]
for i in range(sheet.nrows):
    x1.append(sheet.cell_value(i, 0))
    y.append(sheet.cell_value(i, 1))
    z.append(sheet.cell_value(i, 2))

x2 = [x1[x:x + 6] for x in range(0, len(x1), 6)]
x3 = np.array(x2)
y1 = [y[x:x + 6] for x in range(0, len(y), 6)]
y2 = np.array(y1)
z1 = [z[x:x + 6] for x in range(0, len(z), 6)]
z2 = np.array(z1)
print(y2)
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)

img = ax.imshow(z2, origin='lower',  extent=(0.2, 0.5, 0.15, 0.45), vmin=0, vmax=1.0)
for i in range(len(z)):
    ax.scatter(x[i], y[i], z2)
cbar_ax = make_axes_locatable(ax).append_axes(position='right', size='5%', pad=0.1)
cbar = fig.colorbar(mappable=img, cax=cbar_ax)
cbar.set_ticks([0, 50, 100, 150, 200])
cbar.set_ticklabels(['0', '50', '100', '150', '200 nm'])
plt.show()