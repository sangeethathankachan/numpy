import numpy as np
a=np.array([1,2,3])
b=a.copy()
print("b",b)
c=np.array([(2,1,3),(4,1,2)])
d=np.transpose(c)
print("d",d)
print("transpose of d",d.T)
print("c.ravel()",c.ravel())
e=c-a
print("e",e)
print(" reshaping e ",e.reshape(-1))
print("reshaping e ",e.reshape(2,-1))
b=np.array([[0,1],[2,3]])
print("b",b)
