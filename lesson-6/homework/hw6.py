Вопросы:
# Homeworks

## 1. Modify String with Underscores
Given a string `txt`, insert an underscore (`_`) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

### Examples
**Input:** `hello`
**Output:** `hel_lo`

**Input:** `assalom`
**Output:** `ass_alom`

**Input:** `abcabcabcdeabcdefabcdefg`
**Output:** `abc_abcab_cdeabcd_efabcdef_g`

---

## 2. Integer Squares Exercise

### Task
The provided code stub reads an integer, `n`, from STDIN. For all non-negative integers `i` where `0 <= i < n`, print `i^2`.

### Example Input
```
5
```

### Example Output
```
0
1
4
9
16
```

### Input Format
The first and only line contains the integer, `n`.

### Constraints
- `1 <= n <= 20`

### Output Format
Print `n` lines, one corresponding to each `i^2` where `0 <= i < n`.

---

## 3. Loop-Based Exercises

### Exercise 1: Print first 10 natural numbers using a while loop

### Exercise 2: Print the following pattern
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Exercise 3: Calculate sum of all numbers from 1 to a given number
**Example:**
```
Enter number 10
Sum is: 55
```

### Exercise 4: Print multiplication table of a given number
**Example:**
```
2
4
6
8
10
12
14
16
18
20
```

### Exercise 5: Display numbers from a list using a loop
**Given:**
```python
numbers = [12, 75, 150, 180, 145, 525, 50]
```
**Expected Output:**
```
75
150
145
```

### Exercise 6: Count the total number of digits in a number
**Example:**
```
75869
Output: 5
```

### Exercise 7: Print reverse number pattern
```
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
```

### Exercise 8: Print list in reverse order using a loop
**Given:**
```python
list1 = [10, 20, 30, 40, 50]
```
**Expected Output:**
```
50
40
30
20
10
```

### Exercise 9: Display numbers from -10 to -1 using a for loop
```
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
```

### Exercise 10: Display message “Done” after successful loop execution
**Example:**
```python
0
1
2
3
4
Done!
```

### Exercise 11: Print all prime numbers within a range
**Example:**
```
Prime numbers between 25 and 50:
29
31
37
41
43
47
```

### Exercise 12: Display Fibonacci series up to 10 terms
**Example:**
```
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34
```

### Exercise 13: Find the factorial of a given number
**Example:**
```
5! = 120
```

---

## 4. Return Uncommon Elements of Lists
### Task
Return the elements that are not common between two lists. The order of elements does not matter.

### Examples
- **Input:** `list1 = [1, 1, 2], list2 = [2, 3, 4]`  
  **Output:** `[1, 1, 3, 4]`

- **Input:** `list1 = [1, 2, 3], list2 = [4, 5, 6]`  
  **Output:** `[1, 2, 3, 4, 5, 6]`

- **Input:** `list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]`  
  **Output:** `[2, 2, 5]`

Ответы:
# =======================================
# 🧩 Homework 1: Modify String with Underscores
# =======================================

def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0

    for i, ch in enumerate(txt):
        result += ch
        count += 1
        if count == 3 and i < len(txt) - 1:
            # если следующая буква — гласная или уже _, сдвигаем
            if txt[i + 1] in vowels or txt[i + 1] == "_":
                result += txt[i + 1]
                count = 1  # сбрасываем счётчик
            else:
                result += "_"
                count = 0
    return result


print("Homework 1:")
print(insert_underscores("hello"))
print(insert_underscores("assalom"))
print(insert_underscores("abcabcabcdeabcdefabcdefg"))
print("-" * 40)


# =======================================
# 🧩 Homework 2: Integer Squares Exercise
# =======================================

def print_squares(n):
    for i in range(n):
        print(i ** 2)

print("Homework 2:")
print_squares(5)
print("-" * 40)


# =======================================
# 🧩 Homework 3: Loop-Based Exercises
# =======================================

# Exercise 1
print("Exercise 1:")
i = 1
while i <= 10:
    print(i)
    i += 1
print("-" * 20)

# Exercise 2: Pattern
print("Exercise 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("-" * 20)

# Exercise 3: Sum 1..n
print("Exercise 3:")
n = 10
print("Sum is:", sum(range(1, n + 1)))
print("-" * 20)

# Exercise 4: Multiplication table
print("Exercise 4:")
num = 2
for i in range(1, 11):
    print(num * i)
print("-" * 20)

# Exercise 5: Filtered list
print("Exercise 5:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n > 500:
        break
    elif n > 150:
        continue
    elif n % 5 == 0:
        print(n)
print("-" * 20)

# Exercise 6: Count digits
print("Exercise 6:")
num = 75869
print("Total digits:", len(str(num)))
print("-" * 20)

# Exercise 7: Reverse pattern
print("Exercise 7:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
print("-" * 20)

# Exercise 8: Reverse list
print("Exercise 8:")
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)
print("-" * 20)

# Exercise 9: From -10 to -1
print("Exercise 9:")
for i in range(-10, 0):
    print(i)
print("-" * 20)

# Exercise 10: Done message
print("Exercise 10:")
for i in range(5):
    print(i)
else:
    print("Done!")
print("-" * 20)

# Exercise 11: Prime numbers
print("Exercise 11:")
start, end = 25, 50
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
print("-" * 20)

# Exercise 12: Fibonacci
print("Exercise 12:")
n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n" + "-" * 20)

# Exercise 13: Factorial
print("Exercise 13:")
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")
print("-" * 40)


# =======================================
# 🧩 Homework 4: Return Uncommon Elements of Lists
# =======================================

def uncommon_elements(list1, list2):
    result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
    return result

print("Homework 4:")
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
print("-" * 40)

