data = df['stroke'].value_counts()
data.plot(kind='pie', autopct='%.2f%%')
plt.show()
