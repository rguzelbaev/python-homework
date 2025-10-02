
Homework: List and Tuple Exercises
Вопросы:
1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.

2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.

3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.

5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.

6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.

7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.

8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.

10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".

11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.

12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.

13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.

14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.

15. Reverse a Tuple
Create a tuple of words and print it in reverse order.

--ответы:
# 1. Create and Access List Elements
fruits = ["apple", "banana", "orange", "grape", "mango"]
print("Третий фрукт:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Объединенный список:", merged_list)

# 3. Extract Elements from a List
nums = [10, 20, 30, 40, 50, 60, 70]
new_list = [nums[0], nums[len(nums)//2], nums[-1]]
print("Новый список:", new_list)

# 4. Convert List to Tuple
movies = ["Inception", "Titanic", "Avatar", "Matrix", "Interstellar"]
movies_tuple = tuple(movies)
print("Кортеж фильмов:", movies_tuple)

# 5. Check Element in a List
cities = ["London", "New York", "Paris", "Tokyo"]
print("Есть ли Paris в списке?", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
dup_list = nums * 2
print("Дублированный список:", dup_list)

# 7. Swap First and Last Elements of a List
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("После обмена:", nums)

# 8. Slice a Tuple
numbers = tuple(range(1, 11))
print("Срез 3:7:", numbers[3:8])

# 9. Count Occurrences in a List
colors = ["blue", "red", "green", "blue", "yellow", "blue"]
print("Количество 'blue':", colors.count("blue"))

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
print("Индекс 'lion':", animals.index("lion"))

# 11. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged_tuple = t1 + t2
print("Объединенный кортеж:", merged_tuple)

# 12. Find the Length of a List and Tuple
l = [1, 2, 3, 4]
t = (10, 20, 30)
print("Длина списка:", len(l))
print("Длина кортежа:", len(t))

# 13. Convert Tuple to List
t = (5, 10, 15, 20, 25)
t_list = list(t)
print("Кортеж в список:", t_list)

# 14. Find Maximum and Minimum in a Tuple
t = (12, 45, 3, 67, 22)
print("Максимум:", max(t))
print("Минимум:", min(t))

# 15. Reverse a Tuple
words = ("one", "two", "three", "four")
print("Реверс кортежа:", words[::-1])

