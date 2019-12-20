import numpy.matlib
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b))
print(np.vdot(a,b))
print(np.inner(np.array([1,2,3]),np.array([0,1,0])))
print(np.inner(a,b))
print(np.matmul(a,b))
c=np.array([[6,1,1],[4,-2,5],[2,8,7]])
print(c)
print(np.linalg.det(c))
