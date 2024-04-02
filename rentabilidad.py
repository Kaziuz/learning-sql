import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Obteniendo los 10 productos mas rentables
conn = sqlite3.connect("Northwind.db") # Nos conectamos a la base de datos
query = '''
  SELECT ProductName, SUM(Price * Quantity) as Revenue
  FROM OrderDetails od
  JOIN Products p ON p.ProductID = od.ProductID
  GROUP BY od.ProductID
  ORDER BY Revenue DESC
  LIMIT 10
'''

top_products = pd.read_sql_query(query, conn)

top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10, 5), legend=False)

plt.title("10 productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# Obteniendo los 10 productos mas efectivos
query2 = '''
  SELECT FirstName || " " || LastName as Employee, count(*) as Total
  FROM Orders o
  JOIN Employees e ON e.EmployeeID = o.EmployeeID
  GROUP BY o.EmployeeID
  ORDER BY Total ASC
  limit 3
'''
top_empleyees = pd.read_sql_query(query2, conn)
top_empleyees.plot(x="Employee", y="Total", kind="bar", figsize=(10, 5), legend=False)

plt.title("Empleados mas efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido")
plt.xticks(rotation=45)
plt.show()
