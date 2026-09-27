sh_kmeans_task = []
for num_clusters in range(2, 6):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_task_scaled)
    score = silhouette_score(X_task_scaled, cluster_labels)
    sh_kmeans_task.append(score)
    print(f"K-Means n_clusters = {num_clusters}, silhouette score = {score}")
