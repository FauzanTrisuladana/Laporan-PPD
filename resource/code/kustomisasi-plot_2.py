x = np.array(["01/02/2020", "01/03/2020", "01/04/2020", "01/05/2020"])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([13, 4, 10, 12])

plt.plot(x, y1, marker='o', label='iot 1')
plt.plot(x, y2, marker='*', label='iot 2')
plt.legend()

plt.ylabel('suhu (C)', fontsize=10)
plt.xlabel('tanggal', fontsize=10)

plt.ylim([-20, 30])
plt.show()