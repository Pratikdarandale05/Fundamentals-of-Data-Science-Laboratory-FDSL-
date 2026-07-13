import numpy as np
my_array = np.array([5,6,7,8], dtype=np.int64)

my_2d_array = np.array([[1,2,3,4],[5,6,7,8]], dtype=np.int64)

my_3d_array = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[9,8,7,6]]], dtype=np.int64)

print("1D array :", my_array)
print ("2D array :", my_2d_array)
print ("3D array :", my_3d_array)
print (my_array.data)
print (my_2d_array.data)
print (my_3d_array.shape)
print (my_3d_array.dtype)
print (my_2d_array.strides)
