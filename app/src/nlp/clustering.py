from sklearn.feature_extraction.text import TfidfVectorizer
import umap
import hdbscan


def cluster_descriptions(texts, n_neighbors=15, min_dist=0.1):
    vec = TfidfVectorizer(max_features=5000)
    X = vec.fit_transform(texts)
    um = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, metric='cosine')
    emb = um.fit_transform(X.toarray())
    clusterer = hdbscan.HDBSCAN(min_cluster_size=10)
    labels = clusterer.fit_predict(emb)
    return labels, emb, vec