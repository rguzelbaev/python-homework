Homework:

Exercise 1: Threaded Prime Number Checker

Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

Exercise 2: Threaded File Processing

Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.


Решения:
Exercise 1: Threaded Prime Number Checker

Проверка простых чисел в диапазоне с использованием многопоточности (threading)

import threading

# Функция для проверки, простое ли число
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Функция, которую выполняет поток
def find_primes(start, end, result):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result.extend(local_primes)


# Основная программа
if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4
    threads = []
    result = []

    # Делим диапазон между потоками
    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step - 1
        if i == num_threads - 1:  # последний поток берёт остаток
            end = end_range

        t = threading.Thread(target=find_primes, args=(start, end, result))
        threads.append(t)
        t.start()

    # Ожидаем завершения всех потоков
    for t in threads:
        t.join()

    print("Prime numbers:", sorted(result))


Вывод (пример):

Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, ..., 97]

Exercise 2: Threaded File Processing

Подсчёт слов в большом файле с помощью потоков

import threading
from collections import Counter

# Функция для подсчёта слов в тексте
def count_words(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)


if __name__ == "__main__":
    file_path = "big_text.txt"
    num_threads = 4
    threads = []
    counters = []

    # Читаем все строки файла
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Разделяем строки между потоками
    chunk_size = len(lines) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else len(lines)
        thread_lines = lines[start:end]

        t = threading.Thread(target=count_words, args=(thread_lines, counters))
        threads.append(t)
        t.start()

    # Ждём завершения всех потоков
    for t in threads:
        t.join()

    # Объединяем результаты
    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    # Показываем 10 самых частых слов
    print("Top 10 words:")
    for word, count in total_counter.most_common(10):
        print(f"{word}: {count}")

Пример вывода:

Top 10 words:
the: 523
and: 421
to: 398
of: 310
a: 270
...
