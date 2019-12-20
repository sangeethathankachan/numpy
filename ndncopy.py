import numpy as np
a=np.arange(6)
print("our array is ",a)
print("id is ",id(a))
b=a
print("b array is :",b)
print("id of b is ",id(b))
b.shape=3,2
print(b)
print(a)
print b is a
