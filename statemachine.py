import numpy as np
import matplotlib.pyplot as plt

x = np.array( [[0,0,1],
				[0,1,1],
				[1,0,1],
				[1,1,1]])

y = np.array([[0,0,1,1]]).T

# plt.matshow(np.hstack((x,y)), fignum = 10, cmap=plt.cm.gray)
# plt.show()

#sigmoid function
def sigmoid(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))
Xaxis = np.arange(-6,6, 0.1)

plt.plot(Xaxis, sigmoid(Xaxis))
plt.show()