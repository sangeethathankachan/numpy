import numpy as np
a=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
print("median ",np.median(a))
print("median with axis=0 ",np.median(a,axis=0))
print("median with axis=1 ",np.median(a,axis=1))

