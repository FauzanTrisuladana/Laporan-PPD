import seaborn as sns

# Visualize numeric distributions
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(df['price'], bins=50, kde=True, ax=axes[0]).set_title('Price Distribution')
sns.histplot(df['bath'].dropna(), bins=20, kde=False, ax=axes[1]).set_title('Bathrooms Distribution')
sns.histplot(df['balcony'].dropna(), bins=10, kde=False, ax=axes[2]).set_title('Balcony Distribution')
plt.show()
