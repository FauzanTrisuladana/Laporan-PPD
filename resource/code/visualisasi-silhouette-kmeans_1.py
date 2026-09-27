plt.plot(range(2,11),sh_list, marker='o', linewidth=2, markersize=8)
plt.xlabel("Number of Clusters", size=13)
plt.ylabel("silhouette score", size=13)
plt.title("Silhoutte score values vary depending on the number of clusters utilized.")
plt.show()
# di stage ini kita menemukan k=2 dengan score tertinggi
