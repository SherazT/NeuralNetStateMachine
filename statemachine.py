import numpy as py
import matplotlib.pyplot as plt

x = py.array( [[0,0,1],
				[0,1,1],
				[1,0,1],
				[1,1,1]])

y = py.array([[0,0,1,1]]).T

plt.matshow(py.hstack((x,y)), fignum = 10, cmap=plt.cm.gray)
plt.show()