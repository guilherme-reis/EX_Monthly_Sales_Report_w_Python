import pandas as pd
import numpy as np

# Dados fictícios de vendas
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': [15000, 18000, 12000, 25000, 22000, 24000, 26000, 30000, 27000, 29000, 31000, 35000],
    'Quantity': [150, 180, 120, 250, 220, 240, 260, 300, 270, 290, 310, 350],
    'New_Customers': [10, 15, 8, 25, 20, 22, 18, 30, 27, 25, 30, 35],
    'Returning_Customers': [50, 55, 45, 60, 58, 60, 62, 65, 64, 66, 68, 70]
}

# Dados fictícios de produtos
products_data = {
    'Product_ID': [1, 2, 3, 4, 5],
    'Product_Name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Price': [100, 150, 200, 250, 300],
    'Stock': [30, 50, 20, 10, 40]
}

# Criar dataframes
df_sales = pd.DataFrame(sales_data)
df_products = pd.DataFrame(products_data)

# Salvar os dataframes como CSV
df_sales.to_csv('monthly_sales_report/data/sales_data.csv', index=False)
df_products.to_csv('monthly_sales_report/data/products_data.csv', index=False)

print("CSV files created successfully!")
