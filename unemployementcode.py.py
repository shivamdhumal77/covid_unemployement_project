import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("C:\\Users\dhuma\\Desktop\\unemployement project\\Unemployment_in_India.csv")

# Check for missing values
print(data.isnull().sum())

# Plotting unemployment rate
plt.figure(figsize=(10, 6))
sns.barplot(x="states", y="Unemployment Rate (%)", data=data)
plt.title("Indian Unemployment Rate by State")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
