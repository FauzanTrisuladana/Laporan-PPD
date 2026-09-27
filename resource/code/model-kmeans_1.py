# algoritma kmeans menggunakan nilai silhoutte

k_means = KMeans(n_clusters = 2, random_state = 42)
k_means.fit(X_new)
labels = k_means.labels_
df_new['cluster_labels'] = labels
df_new.head()
