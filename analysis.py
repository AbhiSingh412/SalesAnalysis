import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("superstore.csv", encoding='latin1')

print("Initial Data Shape:", df.shape)

# 2. Data Cleaning
df.dropna(inplace=True)                      # remove missing rows
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

print("After Cleaning Shape:", df.shape)

# 3. Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# 4. Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# 5. Region-wise Sales
region_sales = df.groupby('Region')['Sales'].sum()

# =========================
# VISUALIZATIONS
# =========================

# Monthly Sales Trend
plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Top Products
plt.figure()
top_products.plot(kind='barh')
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.show()

# Region Sales
plt.figure()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.show()
