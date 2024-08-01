import sympy
A = sympy.Matrix([[8,3,1],[2,-1,3],[3,1,4]])

try:
    InvA = A.inv()
    print(InvA, A * InvA, sep='\n')
except Exception as message:
    print(message)