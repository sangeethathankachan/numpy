import numpy as np
a=np.arange(1,9).reshape(2,4)
print("array ",a)
print("shape ",a.shape)
b=np.arange(9,17).reshape(2,4)
print("array ",b)
print("shape ",b.shape)
c=np.append(a,b)
print("appended array ",c)
print("shape",c.shape)
c=np.append(a,b,axis=0)
print("appended array with axis 0 ",c)
c=np.append(a,b,axis=1)
print("appended array with axis 1 ",c)
