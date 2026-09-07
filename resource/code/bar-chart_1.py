y = np.array([35, 25, 25, 15])
x = ["Web Programer", "Data Scientist", "DB Admin", "Manager"]

plt.bar(x, y)

plt.xticks(rotation=45)
plt.ylabel('jumlah')
plt.show()