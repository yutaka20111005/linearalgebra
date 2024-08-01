import numpy as np
import numpy.linalg as LA

A = np.array([[4,1,-1],[1,2,-1],[-1,-1,2]])
t = np.pi/4 #これは π/4を意味する

## 1行ごとに [  ] で囲む
R = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])

vals, vecs = LA.eig(A)
print('====固有値 valsと、固有ベクトル vecsを分けた方が見やすい=====')
print("固有値", vals)
print("固有ベクトル", vecs)
print("固有ベクトルを列ベクトルとした行列として表示されるので、")
print("「固有値 5 に対する固有ベクトル」は、上記結果において「縦方法に並んだ」下記となる点に注意する。")
print("8.16496581e-01, 4.08248290e-01, -4.08248290e-01")
print("")
print('========= R ===========')
print(R)
print(LA.eig(R))
print('====固有値 valsと、固有ベクトル vecsを分けた方が見やすい=====')
print(R)
vals,vecs=LA.eig(R)
print("固有値",vals)
print("固有ベクトル",vecs)
