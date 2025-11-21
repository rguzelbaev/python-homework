Вопросы:
Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age
2. Print the first 3 rows of the DataFrame
3. Find the mean age of the individuals
4. Select and print only the 'Name' and 'City' columns
5. Add a new column 'Salary' with random salary values
6. Display summary statistics of the DataFrame

Homework 2:

1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data.
Use below table.

| Month | Sales | Expenses |
|-------|-------|----------|
| Jan   | 5000  | 3000     |
| Feb   | 6000  | 3500     |
| Mar   | 7500  | 4000     |
| Apr   | 8000  | 4500     |


2. Calculate and display the maximum sales and expenses.
3. Calculate and display the minimum sales and expenses.
4. Calculate and display the average sales and expenses.


Homework 3:

1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

| Category       | January | February | March | April |
|----------------|---------|----------|-------|-------|
| Rent           | 1200    | 1300     | 1400  | 1500  |
| Utilities      | 200     | 220      | 240   | 250   |
| Groceries      | 300     | 320      | 330   | 350   |
| Entertainment  | 150     | 160      | 170   | 180   |


2. Calculate and display the maximum expense for each category.
3. Calculate and display the minimum expense for each category.
4. Calculate and display the average expense for each category.

In this task, use `.set_index` method to make Category column as index. 

Try this code, learn it and use it in the task.

> expenses.set_index('Category')


Ответы:
Homework 1 — pandas
import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename columns using a function
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# 2. Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# 3. Find mean age
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# 4. Select and print only the 'first_name' and 'city' columns
print("\nName and City columns:")
print(df[['first_name', 'city']])

# 5. Add new column 'Salary' with random values
df['salary'] = np.random.randint(3000, 10000, size=len(df))
print("\nDataFrame with Salary:")
print(df)

# 6. Display summary statistics
print("\nSummary statistics:")
print(df.describe())

Homework 2 — Sales & Expenses
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

print("DataFrame:")
print(sales_and_expenses)

# 2. Maximum
print("\nMax Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# 3. Minimum
print("\nMin Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# 4. Average
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

Homework 3 — Monthly Expenses
import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Set Category as index
expenses = expenses.set_index('Category')

print("Expenses DataFrame:")
print(expenses)

# 2. Max expense per category
print("\nMaximum expense per category:")
print(expenses.max(axis=1))

# 3. Minimum expense per category
print("\nMinimum expense per category:")
print(expenses.min(axis=1))

# 4. Average expense per category
print("\nAverage expense per category:")
print(expenses.mean(axis=1))
