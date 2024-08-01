import numpy as np
import numpy.linalg as LA

A = np.array([[3,1],[1,3]])
B = np.array([[3,2],[1,4]])
C = np.array([[1,-1],[-1,2]])

print('========= A ===========')
vals,vecs = LA.eig(A)
print(vals)
print(vecs)

print('========= B ===========')
print(LA.eig(B))
print('========= C ===========')
print(LA.eig(C))