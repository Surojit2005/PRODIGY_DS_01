import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\Users\SUROJIT PAUL\OneDrive\Desktop\PRODIGY INFOTECH\task 1\economy.csv"  # Ensure this file is in the same directory
df = pd.read_csv(file_path)

# Bar Chart: GDP by Country
plt.figure(figsize=(12, 6))
sns.barplot(x="GDP (in Trillions USD)", y="Country", data=df, palette="viridis")
plt.xlabel("GDP (in Trillions USD)")
plt.ylabel("Country")
plt.title("Top 15 Economies by GDP (2023)")
plt.show()

# Histogram: GDP Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["GDP (in Trillions USD)"], bins=10, kde=True, color="blue")
plt.xlabel("GDP (in Trillions USD)")
plt.ylabel("Frequency")
plt.title("GDP Distribution of Top 15 Economies (2023)")
plt.show()
