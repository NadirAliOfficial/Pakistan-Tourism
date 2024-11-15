

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("pakistan_tourism_data.csv")
df = pd.DataFrame(data)
df.head()


# <h2>Total Number of Tourists by City</h2>
import matplotlib.pyplot as plt

tourists_by_city = df.groupby('City')['Number of Tourists'].sum().sort_values()

tourists_by_city.plot(kind='barh', color='skyblue')
plt.title('Total Number of Tourists by City')
plt.xlabel('Number of Tourists')
plt.ylabel('City')
plt.show()


# <h2>Tourist Satisfaction by Accommodation</h2>

satisfaction_accommodation = df.groupby('Accommodation Type')['Tourist Satisfaction Rating'].mean()

# Plotting 
satisfaction_accommodation.plot(kind='bar', color='coral', rot=45)
plt.title('Average Tourist Satisfaction by Accommodation Type')
plt.xlabel('Accommodation Type')
plt.ylabel('Average Satisfaction Rating')
plt.show()


# <h2>Monthly Trend of Tourists</h2>
# Group By Month
monthly_tourists = df.groupby('Month')['Number of Tourists'].sum()

# Plotting
monthly_tourists.plot(kind='line', marker='o', color='green')
plt.title('Monthly Trend of Tourists')
plt.xlabel('Month')
plt.ylabel('Number of Tourists')
plt.grid(True)
plt.show()


# <h2>Total revenue by city</h2>
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Total revenue by city
revenue_by_city = (df.groupby('City')['Revenue Generated (PKR)'].sum() / 280).sort_values(ascending=False).head(3)

# Plotting
ax = revenue_by_city.plot(kind='bar', color='purple')
plt.title('Top 3 Cities by Tourism Revenue')
plt.xlabel('City')
plt.ylabel('Revenue Generated (USD)')
plt.xticks(rotation=0)

# y-axis ticks with commas
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'${int(x):,}'))

plt.show()



# <h2>Tourist Expenditures</h2>

# Tourist expenditures
plt.figure(figsize=(10, 6))
plt.hist(df['Tourist Expenditure (PKR)'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of Tourist Expenditures')
plt.xlabel('Tourist Expenditure (PKR)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# <h2>Tourist weather condition</h2>
# Tourist numbers by weather condition
tourists_by_weather = df.groupby('Weather Condition')['Number of Tourists'].sum()

# Pie chart
tourists_by_weather.plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Tourist Count by Weather Condition')
plt.ylabel('')
plt.show()


# <h2>Peak Tourist season</h2>

# Grouping by month
monthly_tourists = df.groupby('Month')['Number of Tourists'].sum().sort_values(ascending=False)

# Plotting
monthly_tourists.plot(kind='bar', color='teal')
plt.title('Tourists per Month (Peak Season Analysis)')
plt.xlabel('Month')
plt.ylabel('Number of Tourists')
plt.xticks(rotation=45)
plt.show()

# Peak Month
peak_month = monthly_tourists.idxmax()
print(f'The peak tourist month is: {peak_month}')
# Total revenue by tourist type
revenue_by_tourist_type = df.groupby('Tourist Type')['Revenue Generated (PKR)'].sum()

# Plotting
revenue_by_tourist_type.plot(kind='pie', autopct='%1.1f%%', colors=['#ffcc99', '#66b3ff'], startangle=140)
plt.title('Revenue Contribution by Tourist Type')
plt.ylabel('') 
plt.show()


# <h2>Top 5 Cities by Tourist Expenditure</h2>
#Total tourist expenditure by top 5 cities
expenditure_by_city = (df.groupby('City')['Tourist Expenditure (PKR)'].sum() / 280).sort_values(ascending=False).head(5)

# Plotting
ax = expenditure_by_city.plot(kind='bar', color='darkorange')
plt.title('Top 5 Cities by Tourist Expenditure')
plt.xlabel('City')
plt.ylabel('Total Expenditure (USD)')
plt.xticks(rotation=45)

#  y-axis ticks with commas and dollar sign
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.show()


# <h2>Tourist Transport</h2>


transport_mode = df.groupby('Transport Mode Preference')['Number of Tourists'].sum()
transport_mode.plot(kind='bar', rot=0)
for i, count in enumerate(transport_mode):
    plt.text(i, count + 0.1, str(count),  ha='center', va='bottom')
plt.show()


# <h2>Tourists By Year</h2>
# Tourists by year
total_tourists = df.groupby('Year')['Number of Tourists'].sum()

# Scatter Plot
plt.scatter(["2021", "2022", "2023"], total_tourists.values, color='blue', s=100, edgecolor='black', alpha=0.7)
plt.title("Total Tourists by Year")
plt.xlabel("Year")
plt.ylabel("Number of Tourists")

plt.grid(True, linestyle='--', alpha=0.6)
for x, y in zip(["2021", "2022", "2023"], total_tourists.values):
    plt.text(x, y, str(y), ha='center', va='bottom', color='darkblue')
plt.show()


# <h2>Total revenue</h2>
#  The total revenue generated from tourism
import inflect
p = inflect.engine()

# In numbers
total_revenue = df['Revenue Generated (PKR)'].sum() / 280
print(f"Total Revenue Generated from Tourism: ${total_revenue:.0f} USD")

# In words
total_revenue_words = p.number_to_words(total_revenue)
print(f"Total Revenue: $ {total_revenue_words} USD")


