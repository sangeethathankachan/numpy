import numpy as np
a=np.arange(5)
print("array is :",a)
print("shape",a.shape)
o=2
b=np.delete(a,o)
print("after deleting the items :",b)
print("shape",b.shape)
o=[1,2]
b=np.delete(a,o)
print("after deleting the items :",b)
print("shape",b.shape)

