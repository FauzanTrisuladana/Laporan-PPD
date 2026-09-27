k_means_optimal = KMeans(n_clusters=3, random_state=42)
df_task['cluster_labels_kmeans'] = k_means_optimal.fit_predict(X_task_scaled)

plt.figure(figsize=(8,6))
sns.scatterplot(x='GEO Region', y='Passenger Count', hue='cluster_labels_kmeans', data=df_task, palette='Set1')
plt.show()
