kneedle_task = KneeLocator(range(1, 11), inertia_kmeans_task, S=1.0, curve='convex', direction='decreasing')
print("Optimal K (Elbow):", kneedle_task.knee)
kneedle_task.plot_knee()
plt.show()
