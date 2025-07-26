import pandas as pd
from kmeans_model import run_kmeans, plot_kmeans
from lda_model import train_lda, display_topics

# Load CSV
df = pd.read_csv("20newsgroups_clean.csv")
texts = df['text'].tolist()

# KMeans
kmeans_model, X = run_kmeans(texts, num_clusters=20)
plot_kmeans(X, kmeans_model)

# LDA
lda_model, vectorizer = train_lda(texts, num_topics=20)
display_topics(lda_model, vectorizer)

print("✅ All tasks done.")
