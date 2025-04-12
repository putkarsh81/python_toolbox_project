import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datas
file_path = 'putkarsh624_17436592088213003.csv'
df = pd.read_csv(file_path)

# Clean the 'Year' column to extract just the year as integer
df['Year'] = df['Year'].str.extract(r'(\d{4})').astype(int)

