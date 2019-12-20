import numpy as np
a=np.array([[11,2,3],[4,5,6],[7,8,9]])
print("rank ",np.linalg.matrix_rank(a))
print("Trace ",np.trace(a))
print("Determinant ",np.linalg.det(a))
print("Inverse ",np.linalg.inv(a))
print("power of the matrix ",np.linalg.matrix_power(a,3))
