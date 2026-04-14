import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load data
df=pd.read_csv("retail_sales_dataset.csv")


# clean data
df["Date"] = pd.to_datetime(df["Date"],dayfirst=True)
# print(df.isnull().sum())
# df=df.drop_duplicates(inplace=True)

# solve spelling issues
df['Gender']=df['Gender'].str.lower().str.strip()
df['Product Category']=df['Product Category'].str.lower().str.strip()
print(df.head())
print(df['Product Category'].unique())
print(df.groupby('Product Category')['Total Amount'].sum())

# descriptive analysis
# print(df.describe())
# print((df["Quantity"] * df["Price per Unit"] == df["Total Amount"]).all())

# trend analysis
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year


# sales trend
df.groupby('Month')['Total Amount'].sum().plot()
plt.show()

# product analysis
df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False).plot(kind='bar')
plt.show()

# Gender analysis
data = df.groupby('Gender')['Total Amount'].sum()

plt.figure()  # clears previous figure

data.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Sales Distribution by Gender")  # correct title
plt.ylabel('')  # remove y-label
plt.tight_layout()

plt.show()

# quantity v/s revenue
sns.scatterplot(x='Quantity',y='Total Amount',data=df)
plt.show()