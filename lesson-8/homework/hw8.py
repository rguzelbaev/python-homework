Вопросы:
# Homework:

# Python Exception Handling: Exercises, Solutions, and Practice

## Exception Handling Exercises

1. Write a Python program to handle a `ZeroDivisionError` exception when dividing a number by zero.

2. Write a Python program that prompts the user to input an integer and raises a `ValueError` exception if the input is not a valid integer.

3. Write a Python program that opens a file and handles a `FileNotFoundError` exception if the file does not exist.

4. Write a Python program that prompts the user to input two numbers and raises a `TypeError` exception if the inputs are not numerical.

5. Write a Python program that opens a file and handles a `PermissionError` exception if there is a permission issue.

6. Write a Python program that executes an operation on a list and handles an `IndexError` exception if the index is out of range.

7. Write a Python program that prompts the user to input a number and handles a `KeyboardInterrupt` exception if the user cancels the input.

8. Write a Python program that executes division and handles an `ArithmeticError` exception if there is an arithmetic error.

9. Write a Python program that opens a file and handles a `UnicodeDecodeError` exception if there is an encoding issue.

10. Write a Python program that executes a list operation and handles an `AttributeError` exception if the attribute does not exist.

---

# Python File Input Output: Exercises, Practice, Solution

## File Input/Output Exercises

1. Write a Python program to read an entire text file.

2. Write a Python program to read first `n` lines of a file.

3. Write a Python program to append text to a file and display the text.

4. Write a Python program to read last `n` lines of a file.

5. Write a Python program to read a file line by line and store it into a list.

6. Write a Python program to read a file line by line and store it into a variable.

7. Write a Python program to read a file line by line and store it into an array.

8. Write a Python program to find the longest words.

9. Write a Python program to count the number of lines in a text file.

10. Write a Python program to count the frequency of words in a file.

11. Write a Python program to get the file size of a plain file.

12. Write a Python program to write a list to a file.

13. Write a Python program to copy the contents of a file to another file.

14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

15. Write a Python program to read a random line from a file.

16. Write a Python program to assess if a file is closed or not.

17. Write a Python program to remove newline characters from a file.

18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
   - **Note:** Some words can be separated by a comma with no space.

19. Write a Python program to extract characters from various text files and put them into a list.

20. Write a Python program to generate 26 text files named `A.txt`, `B.txt`, and so on up to `Z.txt`.

21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

Ответы:
🧩 Часть 1. Exception Handling Exercises
# 1. Handle ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Ошибка: деление на ноль недопустимо!")

# --------------------------------------------------------

# 2. Raise ValueError if input not integer
try:
    num = int(input("Введите целое число: "))
    print("Вы ввели:", num)
except ValueError:
    print("Ошибка: это не целое число!")

# --------------------------------------------------------

# 3. Handle FileNotFoundError
try:
    with open("non_existing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Ошибка: файл не найден!")

# --------------------------------------------------------

# 4. Raise TypeError if inputs not numbers
try:
    a = float(input("Введите число A: "))
    b = float(input("Введите число B: "))
    print("Сумма:", a + b)
except ValueError:
    raise TypeError("Ошибка: оба значения должны быть числовыми!")

# --------------------------------------------------------

# 5. Handle PermissionError
try:
    with open("/root/secret.txt", "r") as f:  # пример файла без доступа
        print(f.read())
except PermissionError:
    print("Ошибка: недостаточно прав для доступа к файлу!")

# --------------------------------------------------------

# 6. Handle IndexError
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Ошибка: индекс вне диапазона списка!")

# --------------------------------------------------------

# 7. Handle KeyboardInterrupt
try:
    n = input("Введите число (или нажмите Ctrl+C): ")
    print("Вы ввели:", n)
except KeyboardInterrupt:
    print("\nПрервано пользователем!")

# --------------------------------------------------------

# 8. Handle ArithmeticError
try:
    x = 5 / 0
except ArithmeticError:
    print("Ошибка: арифметическая операция недопустима!")

# --------------------------------------------------------

# 9. Handle UnicodeDecodeError
try:
    with open("text.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Ошибка кодировки: файл содержит не-ASCII символы.")

# --------------------------------------------------------

# 10. Handle AttributeError
try:
    num = 10
    num.append(5)  # у int нет метода append
except AttributeError:
    print("Ошибка: объект не имеет такого атрибута!")

📁 Часть 2. File Input / Output Exercises
# 1. Read entire file
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())

# --------------------------------------------------------

# 2. Read first n lines
n = 3
with open("sample.txt", "r", encoding="utf-8") as f:
    for i in range(n):
        print(f.readline(), end="")

# --------------------------------------------------------

# 3. Append text to a file
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("\nНовая строка добавлена.")
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())

# --------------------------------------------------------

# 4. Read last n lines
n = 2
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# --------------------------------------------------------

# 5. Read file into a list
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)

# --------------------------------------------------------

# 6. Read file into a variable
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# --------------------------------------------------------

# 7. Read file into array (same as list)
with open("sample.txt", "r", encoding="utf-8") as f:
    arr = [line.strip() for line in f]
print(arr)

# --------------------------------------------------------

# 8. Find longest word
with open("sample.txt", "r", encoding="utf-8") as f:
    words = f.read().split()
print("Самое длинное слово:", max(words, key=len))

# --------------------------------------------------------

# 9. Count number of lines
with open("sample.txt", "r", encoding="utf-8") as f:
    print("Количество строк:", len(f.readlines()))

# --------------------------------------------------------

# 10. Count word frequency
from collections import Counter
with open("sample.txt", "r", encoding="utf-8") as f:
    words = f.read().lower().split()
print("Частота слов:", Counter(words))

# --------------------------------------------------------

# 11. Get file size
import os
print("Размер файла (байт):", os.path.getsize("sample.txt"))

# --------------------------------------------------------

# 12. Write a list to a file
my_list = ["яблоко", "банан", "вишня"]
with open("fruits.txt", "w", encoding="utf-8") as f:
    for item in my_list:
        f.write(item + "\n")

# --------------------------------------------------------

# 13. Copy one file to another
with open("sample.txt", "r", encoding="utf-8") as src:
    with open("copy.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())

# --------------------------------------------------------

# 14. Combine corresponding lines of two files
with open("file1.txt", "r", encoding="utf-8") as f1, open("file2.txt", "r", encoding="utf-8") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# --------------------------------------------------------

# 15. Read a random line
import random
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Случайная строка:", random.choice(lines).strip())

# --------------------------------------------------------

# 16. Check if file is closed
f = open("sample.txt", "r", encoding="utf-8")
print("Файл закрыт?", f.closed)
f.close()
print("Файл закрыт?", f.closed)

# --------------------------------------------------------

# 17. Remove newline characters
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
print(lines)

# --------------------------------------------------------

# 18. Count words in text file (with commas)
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read().replace(",", " ")
    words = text.split()
print("Количество слов:", len(words))

# --------------------------------------------------------

# 19. Extract characters from multiple files
import glob
chars = []
for filename in glob.glob("*.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        chars.extend(list(f.read()))
print(chars[:50])  # первые 50 символов

# --------------------------------------------------------

# 20. Generate 26 files A.txt ... Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"File {letter}\n")

# --------------------------------------------------------

# 21. Create alphabet file with specified number of letters per line
letters_per_line = 5
alphabet = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), letters_per_line):
        f.write(alphabet[i:i+letters_per_line] + "\n")
