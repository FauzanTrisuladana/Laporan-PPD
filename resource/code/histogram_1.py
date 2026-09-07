data = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
bins = [0, 25, 50, 75, 100]

plt.hist(data, bins=bins)
plt.title("histogram")
plt.xticks(bins)
plt.xlabel('nilai')
plt.ylabel('jumlah siswa')
plt.show()