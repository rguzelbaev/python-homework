Вопросы:
**Homework Assignment 1: Analyzing Sales Data**

You are given a dataset containing sales data for an e-commerce website. The dataset (`task\sales_data.csv`) has the following columns:

- `Date`: Date of the sale.
- `Product`: Name of the product sold.
- `Category`: Category to which the product belongs.
- `Quantity`: Number of units sold.
- `Price`: Price per unit.

**Tasks:**

1. Group the data by the `Category` column and calculate the following aggregate statistics for each category:
   - Total quantity sold.
   - Average price per unit.
   - Maximum quantity sold in a single transaction.
2. Identify the top-selling product in each category based on the total quantity sold.
3. Find the date on which the highest total sales (quantity * price) occurred.

**Homework Assignment 2: Examining Customer Orders**

You have a dataset (`task\customer_orders.csv`) containing information about customer orders. The dataset has the following columns:

- `OrderID`: Unique identifier for each order.
- `CustomerID`: Unique identifier for each customer.
- `Product`: Name of the product ordered.
- `Quantity`: Number of units ordered.
- `Price`: Price per unit.

**Tasks:**

1. Group the data by `CustomerID` and filter out customers who have made less than 20 orders.
2. Identify customers who have ordered products with an average price per unit greater than $120.
3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

**Homework Assignment 3: Population Salary Analysis**

1. "task\population.db" sqlite database has `population` table.
2. "task\population salary analysis.xlsx" file defines Salary Band categories. <br />
    Read the data from population table and calculate following measures:
    - Percentage of population for each salary category;
    - Average salary in each salary category;
    - Median salary in each salary category;
    - Number of population in each salary category;
3. Calculate the same measures in each State

Note: Use SQL only to select data from database. All the other calculations should be done in python.

Ответы:
✅ Homework Assignment 1 — Analyzing Sales Data
📌 Импорт библиотек
import pandas as pd

📌 Загрузка данных
df = pd.read_csv("task/sales_data.csv")
df.head()

🎯 Task 1 — Group by Category
Группировка и вычисления:
category_stats = df.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
)

print(category_stats)

🎯 Task 2 — Top-selling product in each category
top_products = (
    df.groupby(["Category", "Product"])["Quantity"]
    .sum()
    .reset_index()
)

top_products = (
    top_products.sort_values(["Category", "Quantity"], ascending=[True, False])
    .groupby("Category")
    .first()
)

print(top_products)

🎯 Task 3 — Date with highest total sales (Quantity * Price)
df["TotalSale"] = df["Quantity"] * df["Price"]

date_sales = df.groupby("Date")["TotalSale"].sum()

max_sales_date = date_sales.idxmax()
max_sales_value = date_sales.max()

print("Date with highest sales:", max_sales_date)
print("Total sales:", max_sales_value)

✅ Homework Assignment 2 — Customer Orders
📌 Загрузка данных
df = pd.read_csv("task/customer_orders.csv")
df.head()

🎯 Task 1 — Customers with ≥ 20 orders
order_count = df.groupby("CustomerID")["OrderID"].count()

customers_20_plus = order_count[order_count >= 20]

print(customers_20_plus)

🎯 Task 2 — Customers with avg product price > $120
avg_price_per_customer = df.groupby("CustomerID")["Price"].mean()

high_price_customers = avg_price_per_customer[avg_price_per_customer > 120]

print(high_price_customers)

🎯 Task 3 — Total quantity & total price per product; filter quantity < 5
product_stats = df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
)

filtered_products = product_stats[product_stats["total_quantity"] >= 5]

print(filtered_products)

✅ Homework Assignment 3 — Population Salary Analysis
📌 Импорт sqlite и данных
import sqlite3
import pandas as pd

conn = sqlite3.connect("task/population.db")
df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

df.head()

📌 Загрузка Salary Bands

Файл Excel содержит диапазоны типа:

Category	Min	Max
salary_bands = pd.read_excel("task/population salary analysis.xlsx")
salary_bands

📌 Функция: определить категорию зарплаты
def get_salary_band(salary):
    row = salary_bands[(salary_bands["Min"] <= salary) & (salary <= salary_bands["Max"])]
    if len(row) == 0:
        return "Unknown"
    return row["Category"].values[0]

df["SalaryCategory"] = df["Salary"].apply(get_salary_band)

🎯 Task: Measures for each Salary Category
Percentage, average salary, median, population count:
category_stats = df.groupby("SalaryCategory").agg(
    population_count=("Salary", "count"),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median")
)

total_population = len(df)
category_stats["percentage"] = (category_stats["population_count"] / total_population) * 100

print(category_stats)

🎯 Task: Same measures by State
state_category_stats = df.groupby(["State", "SalaryCategory"]).agg(
    population_count=("Salary", "count"),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median")
)

state_totals = df.groupby("State")["Salary"].count()

state_category_stats["percentage"] = (
    state_category_stats["population_count"] / state_category_stats.index.get_level_values("State").map(state_totals)
) * 100

print(state_category_stats)


