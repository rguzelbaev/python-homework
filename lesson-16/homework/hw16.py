Вопросы:
# 1. Convert List to 1D Array

Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

Expected Output:

Original List: [12.23, 13.32, 100, 36.32]
One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]


# 2. Create 3x3 Matrix (2?10)

Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

Expected Output:

[[ 2 3 4]
[ 5 6 7]
[ 8 9 10]]


# 3. Null Vector (10) & Update Sixth Value

Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]


# 4. Array from 12 to 38

Write a NumPy program to create an array with values ranging from 12 to 38.

Expected Output:

[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]


# 5. Convert Array to Float Type

Write a NumPy program to convert an array to a floating type.

Sample output:

Original array
[1, 2, 3, 4]


# 6. Celsius to Fahrenheit Conversion

Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

Sample Array [0, 12, 45.21, 34, 99.91]
[-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

Expected Output:

Values in Fahrenheit degrees:
[ 0. 12. 45.21 34. 99.91 32. ]

Values in Centigrade degrees:
[-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Centigrade degrees:
[-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Fahrenheit degrees:
[-0. 12. 45.21 34. 99.91 32. ]


# 7. Append Values to Array (Do self-tudy)

Write a NumPy program to append values to the end of an array.

Expected Output:

Original array:
[10, 20, 30]

After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]


# 8. Array Statistical Functions (Do self-tudy)

Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.


# 9 Find min and max 

Create a 10x10 array with random values and find the minimum and maximum values.

# 10 

Create a 3x3x3 array with random values.

  #Ответы 
  import numpy as np

print("\n===== 1. Convert List to 1D Array =====")
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)


print("\n===== 2. Create 3x3 Matrix (2–10) =====")
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


print("\n===== 3. Null Vector (10) & Update Sixth Value =====")
null_vec = np.zeros(10)
print(null_vec)

null_vec[5] = 11
print("Updated vector:", null_vec)


print("\n===== 4. Array from 12 to 38 =====")
arr_12_38 = np.arange(12, 38)
print(arr_12_38)


print("\n===== 5. Convert Array to Float Type =====")
arr_int = np.array([1, 2, 3, 4])
print("Original array:", arr_int)
arr_float = arr_int.astype(float)
print("Array float:", arr_float)


print("\n===== 6. Celsius → Fahrenheit =====")
celsius = np.array([0, 12, 45.21, 34, 99.91, 0])
fahrenheit = (celsius * 9/5) + 32

print("Values in Celsius:")
print(celsius)

print("Values in Fahrenheit degrees:")
print(fahrenheit)


print("\n===== 7. Append Values to Array =====")
base = np.array([10, 20, 30])
added = np.append(base, [40, 50, 60, 70, 80, 90])

print("Original array:", base)
print("After append:", added)


print("\n===== 8. Mean, Median, Std Dev =====")
rand_arr = np.random.rand(10)
print("Array:", rand_arr)
print("Mean:", np.mean(rand_arr))
print("Median:", np.median(rand_arr))
print("Std Dev:", np.std(rand_arr))


print("\n===== 9. Min & Max of 10x10 =====")
arr_10x10 = np.random.rand(10, 10)
print("Min:", arr_10x10.min())
print("Max:", arr_10x10.max())


print("\n===== 10. 3x3x3 Random Array =====")
arr_3x3x3 = np.random.rand(3, 3, 3)
print(arr_3x3x3)


  
