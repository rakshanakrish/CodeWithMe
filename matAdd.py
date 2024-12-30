import numpy as np
x= np.array([[1,2],[2,3]])
y= np.array([[3,1],[1,1]])
result = np.dot(x,y)#x@y
transpose_matrix = result.T
print(result)
print(transpose_matrix)