import sympy
A = sympy.Matrix([[1,2,1],[2,-1,3],[3,1,4]])

try:
    InvA = A.inv()
    print(InvA, A * InvA, sep='\n')
except Exception as message:
    print(message)

##　手動計算(吐き出し法、ケラスの式)を使って,
##  すぐに、 0 という値が得られます。