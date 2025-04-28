import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datas
file_path = 'putkarsh624_17436592088213003.csv'
df = pd.read_csv(file_path)

# Clean the 'Year' column to extract just the year as integer
df['Year'] = df['Year'].str.extract(r'(\d{4})').astype(int)

# Objective 1: Relationship Between Ration Cards Issued and Food Grains Distributed
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Ration Cards Issued (UOM:Number)', y='Distribution Of Food Grains (UOM:MT(Metrictonne))', hue='Year', palette='viridis')
plt.title('Ration Cards Issued vs Food Grains Distributed')
plt.xlabel('Ration Cards Issued')
plt.ylabel('Food Grains Distributed (MT)')
plt.grid(True)
plt.tight_layout()
plt.show()
# Objective 2: Top 10 States with Highest Food Grains Distribution
top_states = df.groupby('State')['Distribution Of Food Grains (UOM:MT(Metrictonne))'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='mako')
plt.title('Top 10 States by Food Grains Distribution')
plt.xlabel('Total Food Grains Distributed (MT)')
plt.ylabel('State')
plt.tight_layout()
plt.show()
