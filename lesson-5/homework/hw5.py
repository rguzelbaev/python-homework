Homework:
#Вопросы
1.
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



## 2. Conditional Statements Exercise

Given an integer, `n`, perform the following conditional actions:

- If `n` is **odd**, print `Weird`
- If `n` is **even** and in the inclusive range of **2 to 5**, print `Not Weird`
- If `n` is **even** and in the inclusive range of **6 to 20**, print `Weird`
- If `n` is **even** and **greater than 20**, print `Not Weird`

## Input Format
A single line containing a positive integer, `n`.

## Constraints
- `1 <= n <= 100`

## Output Format
Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

## Sample Input 0
```
3
```

## Sample Output 0
```
Weird
```


3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop. 

Give two solutions.

Solution 1 with if-else statement.

Solution 2 without if-else statement.


#Ответы:

🧮 1. Leap Year Function
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Пример:
print(is_leap(2024))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True

⚙️ 2. Conditional Statements Exercise
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


🧾 Примеры:

Ввод	Вывод
3	Weird
4	Not Weird
10	Weird
22	Not Weird
🔢 3. Even Numbers Between a and b (без цикла)
✅ Solution 1: with if–else
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Проверим порядок
if a > b:
    a, b = b, a

evens = list(range(a + (a % 2), b + 1, 2))
print(evens)


🧠 Логика:

a + (a % 2) делает a чётным стартом.

range(..., ..., 2) идёт с шагом 2 без цикла for.

✅ Solution 2: without if–else
a = int(input("Enter a: "))
b = int(input("Enter b: "))

evens = list(range(min(a, b) + (min(a, b) % 2), max(a, b) + 1, 2))
print(evens)


📘 Этот способ делает то же самое, но без использования if–else,
используя только функции min() и max().


