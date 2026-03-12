def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    num_features = len(points[0])
    
    new_centroids = [[0.0] * num_features for _ in range(k)]
    counts = [0] * k

    for point, cluster_idx in zip(points, assignments):
        counts[cluster_idx] += 1
        for d in range(num_features):
            new_centroids[cluster_idx][d] += point[d]

    for i in range(k):
        if counts[i] > 0:
            for d in range(num_features):
                new_centroids[i][d] /= counts[i]
        else:

            pass

    return new_centroids
            
            