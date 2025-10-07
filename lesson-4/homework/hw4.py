Вопросы:
Homeworks:

# Python Dictionary and Set Exercises

## Dictionary Exercises

### 1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.

### 2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.

**Sample Dictionary:**
```python
{0: 10, 1: 20}
```

**Expected Result:**
```python
{0: 10, 1: 20, 2: 30}
```

### 3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.

**Sample Dictionaries:**
```python
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
```

**Expected Result:**
```python
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

### 4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.

**Sample Dictionary (n = 5):**
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

**Expected Output:**
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
```

## Set Exercises

### 1. Create a Set
Write a Python program to create a set.

### 2. Iterate Over a Set
Write a Python program to iterate over sets.

### 3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.

### 4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.

### 5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.

    Ответы:
🧭 Dictionary Exercises
# 1. Sort a Dictionary by Value
d = {'a': 3, 'b': 1, 'c': 2}
asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

# 2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print(d)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = {}
for d in (dic1, dic2, dic3):
    new_dic.update(d)
print(new_dic)

# 4. Generate a Dictionary with Squares
n = 5
d = {x: x**2 for x in range(1, n+1)}
print(d)

# 5. Dictionary of Squares (1 to 15)
d = {x: x**2 for x in range(1, 16)}
print(d)

🌿 Set Exercises
# 1. Create a Set
my_set = {1, 2, 3, 4}
print(my_set)

# 2. Iterate Over a Set
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
my_set = {"a", "b", "c"}
my_set.add("d")
my_set.update(["e", "f"])
print(my_set)

# 4. Remove Item(s) from a Set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

# 5. Remove an Item if Present in the Set
my_set = {1, 2, 3, 4}
my_set.discard(3)  # не вызывает ошибку, если элемента нет
print(my_set)

