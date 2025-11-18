import numpy as np

# 构造numpy数组
x = np.array([1.0,2.0,3.0])
print(x)
print(type(x))

# 数组运算 element-wise，注意数组长度需要相同！
y = np.array([2.0,4.0,6.0])
z = x + y
print(z)
print(x - y)
print(x * y)
print(x / y)

# 数组运算 broadcast
x = np.array([1.0,2.0,3.0])
print(x / 2.0)

# N维数组
A = np.array([[1,2],[3,4]])
print(A)
print(np.ndim)
print(A.shape)
print(A.dtype)

# N维数组也可以进行广播
print(A * 10)
B = np.array([10,20])
print(A * B)

# 访问元素
X = np.array([[51,55],[14,19],[0,4]])
print(X)
print(X[1])
print(X[1][1])

# 拍平
X = X.flatten()
print(X)

# mask
print(X > 15)
print(X[X > 15])

# 矩阵乘法
A = np.array([[1,2],[3,4]])
print(A.shape)
B = np.array([[5,6],[7,8]])
print(B.shape)
C = np.dot(A, B)
print(C)