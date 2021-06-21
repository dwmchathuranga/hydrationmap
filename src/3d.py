from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
cs_values = [103.43, 74.29, 86.63, 68.23, 77.26, 61.23, 103.5, 55.09, 72.9, 83.23, 75.7, 60.48, 101.0, 71.7, 84.44,
             71.9, 69.85, 60.3]  # chemical shifts values which read from spectrum
# cs_values = [103.43, 74.29, 86.63, 68.23, 77.26, 61.23]  # chemical shifts values which read from spectrum
d = [cs_values[x:x + 6] for x in range(0, len(cs_values), 6)]
z = []
y = []
x = []
a=[]
# INADEQUATE-PDSD
for i in range(len(d)):
    for n in range(5):
        z.extend([d[i][n] + d[i][n + 1]] * 6)
    for n in range(6):
        x.extend([d[i][n]] * 6)
        for j in range(6):
            y.append(d[i][j])
    if len(z) < len(x):
        t = len(x)-len(z)
        z.extend([z[-1]] * t)


print(x)
print(y)
for i in y:
    if i == 74:
        a.append(y[i])
print(a)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(z)):
    ax.scatter(x[i], y[i], z[i])
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
ax.set_xlabel('w2')
ax.set_ylabel('w1')
ax.set_zlabel('w3')
plt.show()
