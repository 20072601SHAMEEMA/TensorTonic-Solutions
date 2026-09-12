import numpy as np

def silhouette_score(X: list, labels: list[int]) -> float:
    X = np.array(X)
    labels = np.array(labels)
    
   
    diff = X[:, None, :] - X[None, :, :]
    dist = np.linalg.norm(diff, axis=-1)
    
    n = len(X)
    a = np.zeros(n)
    b = np.full(n, np.inf)
    
    unique_labels = np.unique(labels)
    
    for k in unique_labels:
        cluster_mask = (labels == k)
        
        #
        in_cluster_dists = dist[cluster_mask][:, cluster_mask]
        a[cluster_mask] = np.sum(in_cluster_dists, axis=1) / (np.sum(cluster_mask) - 1)
        
       
        out_cluster_mask = ~cluster_mask
        if np.any(out_cluster_mask):
            out_cluster_dists = dist[out_cluster_mask][:, cluster_mask]
            mean_dists_to_k = np.mean(out_cluster_dists, axis=1)
            b[out_cluster_mask] = np.minimum(b[out_cluster_mask], mean_dists_to_k)
            
   
    s = (b - a) / np.maximum(a, b)
    
    return float(np.mean(s))