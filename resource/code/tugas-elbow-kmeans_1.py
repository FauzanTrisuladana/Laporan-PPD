inertia_kmeans_task = []
for num_clusters in range(1, 11):
    kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans_model.fit(X_task_scaled)
    inertia_kmeans_task.append(kmeans_model.inertia_)
    print(f"n_clusters = {num_clusters}, inertia = {kmeans_model.inertia_}")
