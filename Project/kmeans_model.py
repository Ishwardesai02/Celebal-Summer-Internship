from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def run_kmeans(texts, num_clusters=10):
    vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000, stop_words='english')
    X = vectorizer.fit_transform(texts)

    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(X)

    return model, X

def plot_kmeans(X, model):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(X.toarray())

    plt.figure(figsize=(10,6))
    plt.scatter(reduced[:, 0], reduced[:, 1], c=model.labels_, cmap='rainbow')
    plt.title("KMeans Clustering on TF-IDF Vectors")
    plt.savefig("kmeans_plot.png")
