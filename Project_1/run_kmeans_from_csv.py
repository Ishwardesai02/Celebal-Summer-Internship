# filename: run_kmeans_from_csv.py

import pandas as pd
from kmeans_model import run_kmeans, plot_kmeans  # Assuming it's in the same dir or add to path

# Step 1: Load the data
df = pd.read_csv("20newsgroups_clean.csv")

# Step 2: Extract text
texts = df['text'].tolist()

# Step 3: Run KMeans
model, X = run_kmeans(texts, num_clusters=20)  # You can tweak number of clusters

# Step 4: Plot results
plot_kmeans(X, model)

print("✅ KMeans clustering done. Plot saved as 'kmeans_plot.png'")
