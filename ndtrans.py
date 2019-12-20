import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[3,4],[1,2]])
print("element wise square root is ",np.sqrt(x))
print("element wise square root is ",np.sqrt(y))
print("summation of matrix :",np.sum(x))
print("summation of matrix :",np.sum(y))
print("summation in column wise :",np.sum(x,axis=0))
print("summation in column wise :",np.sum(y,axis=0))
print("summation in row wise :",np.sum(x,axis=1))
print("summation in row wise :",np.sum(y,axis=1))
print("transpose of the matrix :",x.T)
print("transpose of the matrix :",y.T)

