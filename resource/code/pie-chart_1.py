y = np.array([35, 25, 25, 15])
mylables = ["Web Programer", "Data Scientist", "DB Admin", "Manager"]

plt.pie(y, labels=mylables, autopct='%.2f%%')
plt.show()