from matplotlib import pyplot as plt
import pandas as pd

# Load data
file = 'vehicle_sales_trends\sales_data.csv'
df = pd.read_csv(file, thousands=',')

# Identify columns containing yearly sales
sales_cols = [col for col in df.columns if 'Sales' in col]

# Calculate total sales per country
df['Total Sales'] = df[sales_cols].sum(axis=1)

# Sort dataframe by total sales
df_sorted = df.sort_values(by='Total Sales', ascending=False)

# Select top 5 countries
top_five = df_sorted.head(5)
top_countries = top_five['Country']
top_sales_values = top_five['Total Sales']

# PREPARE YEARLY DATA FOR LINE CHART
# Transpose yearly sales so that rows = years, columns = countries
yearly_data = df.set_index('Country')[sales_cols].T
yearly_data.index = [col.replace(' Sales', '') for col in yearly_data.index]
yearly_data = yearly_data[top_countries]  # Top 5 only

# PLOT SETUP 
fig, plots = plt.subplots(1, 3, figsize=(14, 6))

# 1 PIE CHART (Market Share) 
plots[0].pie(top_sales_values, labels=top_countries, autopct='%1.1f%%',startangle=140,
    colors=plt.cm.tab10.colors)

plots[0].set_title('Market Share of Top 5 Countries (2005 to 2022)', fontsize=13, fontweight='bold')

# 2 BAR CHART (Total Sales) 
plots[1].bar(top_five['Country'],top_five['Total Sales'],color='royalblue', width=0.6)
plots[1].set_title('Total Vehicle Sales (Top 5 Countries, 2005 to 2022)', fontsize=13, fontweight='bold')
plots[1].set_ylabel('Total Sales')
plots[1].set_xlabel('Country')
plots[1].tick_params(axis='x', rotation=45)

# 3️ LINE CHART
for country in yearly_data.columns:
    plots[2].plot(yearly_data.index, yearly_data[country], marker='o', label=country)

plots[2].set_title('Yearly Sales Trend (Top 5 Countries)', fontsize=13, fontweight='bold')
plots[2].set_xlabel('Year')
plots[2].set_ylabel('Sales')
plots[2].legend()
plots[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
