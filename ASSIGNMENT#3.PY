# SAVING ANG WRITING FILE USING NUMPY


import numpy as np


# Ex. 1 -  Saving the array to a text File
my_array = np.array([[3, 11, 5], [5, 27, 6], [5, 14, 9]])
np.save('array.txt', my_array)

print()

#Ex. 2 - Saving the array to a Binary File
my_array = np.array([[3,6,9 ], [2,4,6], [5,10,15]])
np.save('array.npy', my_array)

print()

# Ex. 3 -  Saving the array to a Compressed File
my_array1 = np.array([[9,6,3 , ], [1, 2, 3]])
my_array2 = np.array([[5, 1, 6], [1, 6, 8]])
np.savez_compressed('arrays.npz', array1=my_array1, array2=my_array2)

print()

# LOADING DATA FROM FILES USING NUMPY

# Ex.1 - Loading the array from a Text File
my_array = np.loadtxt('array.csv')
print("On my way:", my_array)

print()

#Ex. 2 - Loading the array from a Binary File
my_array = np.load('array.npy')
print("On my way:", my_array)

print()

# Ex. 3 - Loading the arrays from a compressed file
my_array = np.load('arrays.npz')
my_array1 = my_array['array1']
my_array2 = my_array['array2']
print("On my way:", my_array1, my_array2)