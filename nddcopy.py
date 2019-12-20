import numpy as np
a=np.arange(8).reshape(2,2,2)
print("a",a)
print("id a",id(a))
b=a.copy()
print("b",b)
print("id b",id(b))
print b is a #false
b[0,0]=200
print("b ",b)
print("a",a)
