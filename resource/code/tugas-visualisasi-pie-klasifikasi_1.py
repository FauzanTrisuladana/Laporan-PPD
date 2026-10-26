# cek persentase target class
data = df['Occupancy'].value_counts()
data.plot(kind='pie', autopct='%.2f%%')
plt.show()
